import streamlit as st
import pandas as pd
from analysis import load_data, generate_association_rules

def main():
    st.title("Market Basket Analysis")
    
    st.sidebar.header("Upload Transaction Data")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        data = load_data(uploaded_file)
        st.write("Data Loaded Successfully!")
        st.dataframe(data)
        
        if st.sidebar.button("Generate Association Rules"):
            rules = generate_association_rules(data)
            st.write("Association Rules Generated:")
            st.dataframe(rules)

if __name__ == "__main__":
    main()