import pandas as pd
import numpy as np
import os
from sklearn.cluster import KMeans

# --- 1. Load Data ---
fg_df = pd.read_csv('fear_greed_index.csv')
trade_df = pd.read_csv('historical_data.csv')

# --- 2. Clean and Align Dates ---
fg_df['date'] = pd.to_datetime(fg_df['date']).dt.normalize()
trade_df['datetime'] = pd.to_datetime(trade_df['Timestamp IST'], dayfirst=True)
trade_df['date'] = trade_df['datetime'].dt.normalize()

# Merge
df = pd.merge(trade_df, fg_df[['date', 'classification', 'value']], on='date', how='inner')

# --- 3. Metric Creation ---
df['is_win'] = df['Closed PnL'] > 0
daily_metrics = df.groupby(['date', 'classification', 'Account']).agg(
    daily_pnl=('Closed PnL', 'sum'),
    win_rate=('is_win', 'mean'),
    avg_trade_size=('Size USD', 'mean'),
    trade_count=('Order ID', 'count')
).reset_index()

# Add Long/Short Ratio
side_counts = df.groupby(['date', 'Side']).size().unstack(fill_value=0)
side_counts['long_short_ratio'] = side_counts.get('BUY', 0) / side_counts.get('SELL', 1)
daily_metrics = daily_metrics.merge(side_counts[['long_short_ratio']], on='date')

# --- 4. Predictive & Clustering ---
# Clustering: Group traders into 3 archetypes
cluster_data = daily_metrics[['trade_count', 'avg_trade_size', 'win_rate']].fillna(0)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
daily_metrics['archetype'] = kmeans.fit_predict(cluster_data)

# Predictive Feature Preparation
daily_metrics = daily_metrics.sort_values(['Account', 'date'])
daily_metrics['next_day_pnl'] = daily_metrics.groupby('Account')['daily_pnl'].shift(-1)
daily_metrics['is_profitable_next'] = (daily_metrics['next_day_pnl'] > 0).astype(int)

# --- 5. Save for Dashboard ---
daily_metrics.to_csv('daily_metrics.csv', index=False)
print("Analysis complete. 'daily_metrics.csv' saved with 'archetype' column.")