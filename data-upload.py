import streamlit as st
import pandas as pd
from io import StringIO

# Load default CSV data from GitHub
default_data_url = "https://raw.githubusercontent.com/your_username/your_repository/master/evProfile.csv"
data = pd.read_csv(default_data_url)

# Display default data
st.write("Default Data")
st.dataframe(data)

# Edit data in the sidebar
st.sidebar.header('Edit Data')
new_data_text = st.sidebar.text_area('Edit Data (CSV format)', value=data.to_csv(index=False), height=300)

# Apply changes to the data
if st.sidebar.button('Apply Changes'):
    try:
        new_data = pd.read_csv(StringIO(new_data_text))
        data = new_data
        st.success("Data updated successfully.")
    except Exception as e:
        st.error(f"Error: {e}")

# Generate a plot based on the data
if st.sidebar.button('Generate Plot'):
    st.line_chart(data)
