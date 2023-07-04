import streamlit as st
from backend_interactions.user import signup

def render_signup():
    cols = st.columns(2)
    with cols[0]:
        username = st.text_input("Username")
        email = st.text_input("Email")
        full_name = st.text_input("Fullname")
        password = st.text_input("Password", type="password")

        if st.button("Signup"):
            user = {
                "username": username,
                "email": email,
                "full_name": full_name,
                "password": password
            }
            response = signup(user=user)
            if "exists" in response:
                st.warning(response)
            else:
                st.success(response)

def navigate_signup():
    st.session_state.page = render_signup