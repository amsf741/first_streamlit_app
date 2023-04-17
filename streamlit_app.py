import streamlit
streamlit.header('Date Engineering success path')
streamlit.title('Hello World - bravo Alagappan')
streamlit.text('Master SQL')
streamlit.text('Master Snowflake')
streamlit.text('Get certification')
streamlit.text('🥑🍞Get a good job')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
