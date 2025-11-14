# login.py
import streamlit as st
from user_services import authenticate_user

def render_login_page():
    """Renders the login form and navigation to register."""
    st.header("Login")

    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Log In")

        if submitted:
            user = authenticate_user(email, password)
            if user:
                st.success("Logged in successfully!")
                st.session_state.logged_in = True
                st.session_state.email = user["email"]
                st.session_state.role = user["role"]
                st.rerun()
            else:
                st.error("Invalid credentials")
    
    st.markdown("---")
    st.write("Don't have an account?")
    
    # Use a unique key for the button within this module
    if st.button("Sign Up Now", key="signup_redirect"):
        st.session_state.view = 'register'
        st.rerun() 
