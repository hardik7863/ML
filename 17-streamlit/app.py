import pandas as pd
import numpy as np
import streamlit as st

##Title of the application
st.title("Hello Streamlit")

## Display a Simple Text

st.write("This is a simple test")

##Create a simple dataframe

df=pd.DataFrame({
    'First column':[1,2,3,4],
    'second column':[10,20,30,40]
})

# display the dataframe
st.write("here is the dataframe")
st.write(df)

##Create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)