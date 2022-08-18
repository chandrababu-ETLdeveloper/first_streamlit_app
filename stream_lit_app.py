##import streamlit

##streamlit.title('My Parents Healthy Diner')
##streamlit.header('Breakfast menus')
##streamlit.text('🥪sandwich 3 & roti')
##streamlit.text('🥣kale,spinach & dhal')
##streamlit.text('🥚🥚Egg')
##streamlit.text('🍘''Ricecracker')
##streamlit.header('🍉🍎Build your own fruits smoothie🥑🍒')

##import pandas
##my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") ##pull the data to my_fruits_list using pandas##
import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
##streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
# Display the table on the page.




