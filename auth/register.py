import streamlit as st
from db.database import insert_user
from utils.helpers import hash_password

def register():
    st.subheader("Register")

    username = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type="password")
    role = st.selectbox("Register as", ["Student", "Company"])

    if st.button("Register"):
        hashed_pw = hash_password(password)
        insert_user(username, hashed_pw, role)
        st.success("Account created! Please login.")
