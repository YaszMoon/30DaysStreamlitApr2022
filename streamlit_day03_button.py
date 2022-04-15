import streamlit as st

#Create header text for the app
st.header('st.button')

#Conditional statement for alternating message when button pressed
#st.button takes in button label
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')