def clean_data(df):
    # Function to clean the transaction data
    df.dropna(inplace=True)  # Remove missing values
    df['Transaction'] = df['Transaction'].astype(str)  # Ensure Transaction column is string
    return df

def preprocess_data(df):
    # Function to preprocess the transaction data
    # This can include encoding, transforming, or aggregating data as needed
    return df

def plot_results(results):
    # Function to plot the results of the analysis
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.barplot(x='Support', y='Itemset', data=results)
    plt.title('Association Rules Support')
    plt.xlabel('Support')
    plt.ylabel('Itemset')
    plt.show()