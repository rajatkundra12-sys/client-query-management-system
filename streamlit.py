# main.py
import streamlit as st
import login
from register import render_register_page
from Client import show_client_dashboard
from Support import show_support_dashboard

# 1. Initialize session state for the view if it doesn't exist
if 'view' not in st.session_state:
    # Default view is 'login'
    st.session_state.view = 'login'

# # 2. Main app logic to display the correct form based on session state
# st.title("Welcome to Client Query Management")

# # Check the session state and render the appropriate page function
# if st.session_state.view == 'login':
#     login.render_login_page()
# elif st.session_state.view == 'register':
#     render_register_page()

# if st.session_state.logged_in:
#     st.success(f"Logged in as {st.session_state.email} ({st.session_state.role})")
#    # Role-based dashboards
#     if st.session_state.role == "Client":
#         show_client_dashboard()
#     elif st.session_state.role == "Support Team":
#         st.write('support')

# ---------------- Session State ----------------
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.email = None

if 'view' not in st.session_state:
    st.session_state.view = 'login'  # default page

# ---------------- Main App ----------------
if st.session_state.logged_in:
    # User is logged in, show dashboard
    # st.success(f"Logged in as {st.session_state.email} ({st.session_state.role})")
    
    if st.session_state.role == "Client":
        show_client_dashboard()
    elif st.session_state.role == "Support Team":
        show_support_dashboard()
else:
    # User not logged in, show login or register page
    st.title("Welcome to Client Query Management")
    
    if st.session_state.view == 'login':
        login.render_login_page()
    elif st.session_state.view == 'register':
        render_register_page()