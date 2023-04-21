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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

# new section to display fruitvice API response
streamlit.header('Fruityvice Fruit Advice!')
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json()) 

# using json pandas
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# using dataframe
streamlit.dataframe(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text("The fruit load list contains")
#streamlit.text(my_data_row)

streamlit.header("The fruit list contains:")
streamlit.dataframe(my_data_row)
