import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the transaction data.
    - Remove missing values
    - Ensure Transaction column is string
    """
    df.dropna(inplace=True)
    if "Transaction" in df.columns:
        df['Transaction'] = df['Transaction'].astype(str)
    return df


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess the transaction data.
    (You can add encoding, transformation, or aggregation logic here.)
    """
    return df


def plot_results(results: pd.DataFrame, metric: str = "Support"):
    """
    Plot association rule results as a bar chart inside Streamlit.
    
    Parameters
    ----------
    results : DataFrame
        Must contain at least two columns: 'Itemset' and the chosen metric (e.g., Support, Confidence, Lift).
    metric : str
        Which metric to plot on the X-axis. Default = 'Support'.
    """
    if results.empty:
        st.warning("No results to display.")
        return

    if metric not in results.columns:
        st.error(f"Metric '{metric}' not found in results DataFrame.")
        return

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=metric, y='Itemset', data=results, ax=ax, color="skyblue")

    ax.set_title(f'Association Rules by {metric}', fontsize=14)
    ax.set_xlabel(metric, fontsize=12)
    ax.set_ylabel("Itemset", fontsize=12)

    st.pyplot(fig)  # Render in Streamlit
