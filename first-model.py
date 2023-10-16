import streamlit as st
import numpy as np

# Define the function to generate a sine wave
def generate_sine_wave(frequency, num_points):
    x = np.linspace(0, 2 * np.pi, num_points)
    y = np.sin(frequency * x)
    return x, y

# Create a Streamlit web app
st.title('Sine Wave Generator')

# Sidebar to adjust parameters
st.sidebar.header('Adjust Parameters')
frequency = st.sidebar.slider('Frequency', 1, 10, 1)  # Adjust frequency between 1 and 10
num_points = st.sidebar.slider('Number of Points', 50, 500, 100)  # Adjust the number of data points

# Button to generate the sine wave
if st.sidebar.button('Generate Sine Wave'):
    x, y = generate_sine_wave(frequency, num_points)
    
    # Plot the results using st.pyplot()
    st.subheader('Sine Wave Plot')
    st.line_chart(list(zip(x, y))

# Allow editing data
st.sidebar.header('Edit Data')
new_data = st.sidebar.text_area('Enter new data (comma-separated)', value="0,1,2,3,4,5")
new_data = [float(x) for x in new_data.split(',')]

# Display the edited data
st.subheader('Edited Data')
st.write(new_data)

st.write("Note: You can adjust the frequency and number of data points in the sidebar and generate a new sine wave plot.")
