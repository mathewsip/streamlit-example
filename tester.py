import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Create some example data
data = [10, 20, 15, 30]
labels = ['Value 1', 'Value 2', 'Value 3', 'Value 4']

# Create a bar chart using matplotlib
fig, ax = plt.subplots()
ax.bar(labels, data)

# Set labels and title
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_title('Bar Chart Example')

# Display the bar chart in Streamlit
st.pyplot(fig)
