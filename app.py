import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Trader Behavior Analytics", layout="wide")
st.title("📊 Trader Behavior Analytics Dashboard")

# -----------------------------
# Load CSV safely
# -----------------------------
file_path = os.path.join(os.path.dirname(__file__), "daily_metrics.csv")

if not os.path.exists(file_path):
    st.error("❌ daily_metrics.csv not found. Please run main_analysis.py first.")
    st.stop()

df = pd.read_csv(file_path)

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("🔎 Filter Options")

sentiments = sorted(df["classification"].dropna().unique())
selected_sentiment = st.sidebar.multiselect(
    "Select Market Sentiment",
    sentiments,
    default=sentiments
)

filtered_df = df[df["classification"].isin(selected_sentiment)]

if filtered_df.empty:
    st.warning("⚠️ No data available for selected filters.")
    st.stop()

# -----------------------------
# Performance Overview
# -----------------------------
st.subheader("📈 PnL Distribution by Market Sentiment")

fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(
    data=filtered_df,
    x="classification",
    y="daily_pnl",
    ax=ax
)
plt.xticks(rotation=30)
st.pyplot(fig)

# -----------------------------
# Trader Archetypes (SAFE FIX)
# -----------------------------
st.subheader("🧠 Trader Archetypes")

if "archetype" not in filtered_df.columns:
    st.info("ℹ️ Archetype column not found. Using fallback classification.")

    filtered_df["archetype"] = filtered_df["daily_pnl"].apply(
        lambda x: "Profitable" if x > 0 else "Loss-Making"
    )

st.bar_chart(filtered_df["archetype"].value_counts())

# -----------------------------
# Raw Data
# -----------------------------
st.subheader("📋 Raw Metrics")
st.dataframe(filtered_df)