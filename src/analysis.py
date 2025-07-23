def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def generate_association_rules(data, min_support=0.01, min_confidence=0.5):
    from mlxtend.frequent_patterns import apriori, association_rules
    
    # One-hot encode the transaction data
    basket = (data
              .groupby(['TransactionID', 'Item'])
              .size().unstack(fill_value=0)
              .reset_index().set_index('TransactionID'))
    
    # Convert the values to 1s and 0s
    basket = basket.applymap(lambda x: 1 if x > 0 else 0)
    
    # Generate frequent itemsets
    frequent_itemsets = apriori(basket, min_support=min_support, use_colnames=True)
    
    # Generate association rules
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
    
    return rules

def calculate_support(data, item):
    total_transactions = data['TransactionID'].nunique()
    item_transactions = data[data['Item'] == item]['TransactionID'].nunique()
    return item_transactions / total_transactions

def calculate_confidence(data, item_a, item_b):
    total_transactions = data['TransactionID'].nunique()
    item_a_transactions = data[data['Item'] == item_a]['TransactionID'].nunique()
    item_ab_transactions = data[(data['Item'] == item_a) | (data['Item'] == item_b)]['TransactionID'].nunique()
    
    return item_ab_transactions / item_a_transactions if item_a_transactions > 0 else 0

# Additional functions for data processing and analysis can be added here.