# pages/client_dashboard.py
import streamlit as st
import query_services
import user_services
import pandas as pd

def show_client_dashboard():
    
    # Sidebar navigation
    st.sidebar.title("Dashboard")
    page = st.sidebar.radio("Go to", ["Home", "Add Query", "Track Query", "Logout"])

    # Home Page
    if page == "Home":
        st.title("Welcome to the Home Page")

    # Add Query Page
    elif page == "Add Query":
        st.title(" Add Your Query")
        with st.form("query_form"):
            email = st.text_input("Email ID")
            mobile = st.text_input("Mobile Number")
            heading = st.text_input("Query Heading")
            description = st.text_area("Query Description")
            submitted = st.form_submit_button("Submit")

        if submitted:
             email = st.session_state.get("email")
    
             # Check if all fields are filled
        if not email or not heading or not description or not mobile:
                st.warning("Please fill all fields before submitting.")
        else:
                user_id = user_services.get_user_id(email)
                if not user_id:
                    st.error("User ID not found. Please log in again.")
                else:
                    success = query_services.add_query(user_id, email, heading, description, mobile)
                    if success:
                        st.success("Your query has been submitted successfully!")
                    else:
                        st.error("Failed to submit query. Please try again.")

    # Track Query Page
    elif page == "Track Query":
        st.title("Track Your Queries")
        st.write("Here you can check the status of your submitted queries.")

#  Check login
        if "email" not in st.session_state or not st.session_state.email:
            st.warning("Please log in to view your queries.")
            st.stop()

        email = st.session_state.email

        #  Fetch user's queries
        try:
            queries = query_services.get_user_queries(email)
            df = pd.DataFrame(queries)
        except Exception as e:
            st.error(f"Failed to load your queries: {e}")
            st.stop()

        #  Handle empty case
        if df.empty:
            st.info("You have not submitted any queries yet.")
            return

        #  Calculate Open and Closed query counts
        open_count = df[df["status"] == "Open"].shape[0]
        closed_count = df[df["status"] == "Closed"].shape[0]

        #  Two-column layout for stats
        st.markdown("###  Query Summary")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                f"""
                <div style='background-color:#E8F5E9; padding:20px; border-radius:10px; text-align:center;'>
                    <h3 style='color:#2E7D32;'>Open Queries</h3>
                    <h2 style='color:#1B5E20;'>{open_count}</h2>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                f"""
                <div style='background-color:#E3F2FD; padding:20px; border-radius:10px; text-align:center;'>
                    <h3 style='color:#1565C0;'>Closed Queries</h3>
                    <h2 style='color:#0D47A1;'>{closed_count}</h2>
                </div>
                """,
                unsafe_allow_html=True
            )

        # #  Display query table
        # st.markdown("### 🧾 Your Queries")
        # df_display = df.rename(columns={
        #     "query_id": "Query ID",
        #     "heading": "Heading",
        #     "description": "Description",
        #     "status": "Status",
        #     "query_created_time": "Created Time",
        #     "query_closed_time": "Closed Time"
        # })
        # st.dataframe(df_display, use_container_width=True)


    # Logout Page
    elif page == "Logout":
        st.session_state.logged_in = False
        st.session_state.role = None
        st.session_state.email = None
        st.session_state.view = "login"
        st.rerun()
