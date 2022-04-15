# Different ways to use st.write

from turtle import color
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

# Create app header
st.header('st.write')

# Example 1 - a string
st.write('Hello, *World!* :sunglasses:')

# Example 2 - numbers
st.write(1234)

# Example 3 - dataframes
# Define dataframe first then use it as an argument
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write(df)

# Example 4 - multiple arguments
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5 - graph
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns = ['a', 'b', 'c']
)

c = alt.Chart(df2).mark_circle().encode(
    x = 'a', y = 'b', size = 'c', color = 'c', tooltip = ['a', 'b', 'c']
)

st.write(c)
