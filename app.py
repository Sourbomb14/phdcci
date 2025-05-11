import streamlit as st
from auth.login import login
from auth.register import register
from users.student import student_dashboard
from users.company import company_dashboard
from users.admin import admin_dashboard

st.set_page_config(page_title="PHDCCI Internship Portal", layout="wide")

# Session state to track login
if 'user_role' not in st.session_state:
    st.session_state.user_role = None

st.title("🎓 PHDCCI Internship & Placement Portal")

menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Navigation", menu)

if st.session_state.user_role:
    if st.session_state.user_role == "Student":
        student_dashboard()
    elif st.session_state.user_role == "Company":
        company_dashboard()
    elif st.session_state.user_role == "Admin":
        admin_dashboard()
else:
    if choice == "Login":
        login()
    elif choice == "Register":
        register()

