import streamlit as st
import pandas as pd
from io import StringIO
import numpy as np
import matplotlib.pyplot as plt

# Define the function to generate a sine wave
def generate_sine_wave(frequency, num_points):
    x = np.linspace(0, 2 * np.pi, num_points)
    y = np.sin(frequency * x)
    return x, y

# Function to upload and load data
def load_data():
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        return data
    return None

# Main Streamlit app
st.title('Data and Modeling App')
st.markdown('''
    ## Data Upload
    Upload your data for analysis.
    ''')

# First tab for data upload
data = load_data()
if data is not None:
    st.write("Uploaded Data")
    st.dataframe(data)

    st.sidebar.header('Edit Data')
    new_data_text = st.sidebar.text_area('Edit Data (CSV format)', value=data.to_csv(index=False), height=300)

    if st.sidebar.button('Apply Changes'):
        try:
            new_data = pd.read_csv(StringIO(new_data_text))
            data = new_data
            st.success("Data updated successfully.")
        except Exception as e:
            st.error(f"Error: {e}")

# Second tab for modeling
st.markdown('''
    ## Modeling
    Generate a sine wave based on the selected parameters.
    ''')

# Sidebar to adjust parameters for modeling
frequency = st.sidebar.slider('Frequency', 1, 10, 1)
num_points = st.sidebar.slider('Number of Points', 50, 500, 100)

# Button to generate the sine wave
if st.sidebar.button('Generate Sine Wave'):
    x, y = generate_sine_wave(frequency, num_points)

    # Plot the results using st.pyplot()
    st.subheader('Sine Wave Plot')
    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    st.pyplot(plt)

st.write("Note: You can switch between the 'Data Upload' and 'Modeling' tabs to perform the respective tasks.")
