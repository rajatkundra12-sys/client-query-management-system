# register.py
import streamlit as st
from user_services import create_user

def render_register_page():
    """Renders the registration form and navigation to login."""
    st.header("Register")

    with st.form("register_form"):
        name = st.text_input("Username")
        email = st.text_input("Enter Email")
        password = st.text_input("Choose Password", type="password")
        role = st.selectbox("Role", ["Client", "Support Team"], index=None)
        submitted = st.form_submit_button("Register Account")

        if submitted:
            if not name or not email or not password or not role:
                st.warning(" Please fill in all fields.")
            else:
                if create_user(name, email, password, role):
                    st.success(" Account created! Please log in.")
                    st.session_state.view = "login"
                    st.rerun()
                else:
                    st.error(" Email already exists or database error.")

    st.markdown("---")
    st.write("Already have an account?")
    
    # Navigation to login page
    if st.button("Go to Login", key="login_redirect"):
        st.session_state.view = 'login'
        st.rerun()
