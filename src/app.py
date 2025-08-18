import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from analysis import load_data, generate_association_rules
from utils import plot_results

def main():
    st.title("Market Basket Analysis")
    
    st.sidebar.header("Upload Transaction Data")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        data = load_data(uploaded_file)
        st.success("Data Loaded Successfully!")
        st.dataframe(data.head(10))  # Show preview
        
        if st.sidebar.button("Generate Association Rules"):
            rules = generate_association_rules(data)
            
            # Keep only support, confidence, and lift
            rules_display = rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]
            
            st.subheader("Association Rules")
            st.dataframe(rules_display)
            
            # Plot visualization
            st.subheader("Support of Frequent Itemsets")
            fig, ax = plt.subplots(figsize=(8, 6))
            top_rules = rules_display.sort_values("support", ascending=False).head(10)
            ax.barh(top_rules['antecedents'].astype(str), top_rules['support'])
            ax.set_xlabel("Support")
            ax.set_ylabel("Itemsets (Antecedents)")
            ax.set_title("Top 10 Frequent Itemsets by Support")
            st.pyplot(fig)

if __name__ == "__main__":
    main()
