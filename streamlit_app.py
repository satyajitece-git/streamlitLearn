# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(f":cup_with_straw: Customize Your Smoothies :cup_with_straw:")
st.write(
  """Choose the fruit you want in your custom smoothie!
  """
)
name_on_order= st.text_input("Name on smoothie:")
st.write("Name on you smoothie will be : ",name_on_order)
my_dataframe = session.table("smoothies.public.fruit_options").select(col ("FRUIT_NAME"))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list=st.multiselect(
    "Choose up to 5 ingridients:"
    ,my_dataframe
    ,max_selections=5
)
if ingredients_list:
    #st.write(ingredients_list)
    #st.text(ingredients_list)
    #ingredients_list=''
    ingridients_string=''
    for fruit_chosen in ingredients_list:
        ingridients_string += fruit_chosen+' '
        
   # st.write(ingridients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values 
            ('""" + ingridients_string + """','""" + name_on_order + """')"""
  
    time_to_insert=st.button("Submit Order")
    
   # st.write(my_insert_stmt)
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered! '+name_on_order, icon="✅")

cnx = st.connection("snowflake")
session = cnx.session()
