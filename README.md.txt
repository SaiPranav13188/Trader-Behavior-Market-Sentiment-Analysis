Trader Behavior Insights: Hyperliquid & Market Sentiment
This project analyzes the relationship between Bitcoin market sentiment (Fear/Greed) and trading behavior on the Hyperliquid exchange. The objective is to identify how market volatility and sentiment shifts influence trader performance, risk-taking, and strategy execution.

Project Methodology
Data Preparation: Cleaned and aligned high-frequency trade data with daily sentiment indices.

Metric Engineering: Derived performance indicators including daily PnL, Win Rate, and Long/Short ratios.

Behavioral Analysis: Used K-Means Clustering to categorize traders into archetypes (e.g., high-frequency vs. conservative) to uncover hidden performance patterns.

Predictive Modeling: Developed a Random Forest Classifier to predict the likelihood of a trader's profitability based on sentiment and behavioral input.

Key Insights
Sentiment Correlation: Analysis indicates distinct shifts in trade frequency during periods of "Greed," often correlating with lower win rates due to over-leveraging or FOMO.

Behavioral Archetypes: Identified specific trader segments that show higher resilience during "Fear" days, suggesting that patience and mean-reversion strategies are more effective during market downturns.

Strategy Recommendations:

Risk Scaling: Reduce position sizes by ~25% during "Greed" sentiment phases.

Activity Control: Frequent traders should adopt an execution cap during high-volatility regimes to prevent capital erosion.

Setup & Execution
1. Requirements
Ensure you have the necessary libraries installed:

Bash
pip install pandas numpy scikit-learn streamlit seaborn matplotlib
2. Analysis Pipeline
Run the analysis script to process the raw datasets and generate behavioral clusters:

Bash
python main_analysis.py
3. Dashboard Visualization
Launch the Streamlit dashboard to explore the trader metrics, performance distributions, and behavioral archetypes visually:

Bash
python -m streamlit run app.py
Access the dashboard here:

Local URL: http://localhost:8501

Network URL: http://192.168.29.130:8501
