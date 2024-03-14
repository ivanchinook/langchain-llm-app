import langchain_helper as lch
import streamlit as st

st.title("Pets name generator")

user_animal_type=st.sidebar.selectbox("What is your pet?",("Dog","Cat","Cow","Hamster"))

user_pet_color=st.sidebar.text_area(label=f"What color is your {user_animal_type}?", max_chars=15)

if user_pet_color:
    response = lch.generate_pet_name(user_animal_type, user_pet_color)
    st.text(response)
