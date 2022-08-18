##import streamlit

##streamlit.title('My Parents Healthy Diner')
##streamlit.header('Breakfast menus')
##streamlit.text('🥪sandwich 3 & roti')
##streamlit.text('🥣kale,spinach & dhal')
##streamlit.text('🥚🥚Egg')
##streamlit.text('🍘''Ricecracker')
##streamlit.header('🍉🍎Build your own fruits smoothie🥑🍒')

import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)




