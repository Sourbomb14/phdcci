import streamlit as st
from db.database import get_user
from utils.helpers import check_password

def login():
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Login as", ["Student", "Company", "Admin"])
    
    if st.button("Login"):
        user = get_user(username, role)
        if user and check_password(password, user["password"]):
            st.success(f"Welcome {username}!")
            st.session_state.user_role = role
        else:
            st.error("Invalid username or password")
