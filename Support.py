# pages/support_dashboard.py
import streamlit as st
import pandas as pd
import query_services 


def show_support_dashboard():
    """Render the Support Team Dashboard with editable DataFrame and search filters."""

    st.sidebar.title("Support Dashboard")
    page = st.sidebar.radio("Go to", ["All Queries", "Logout"])

    if page == "All Queries":
        st.title("Support Team Dashboard")

        # ----- Fetch data from database -----
        try:
            queries = query_services.get_all_queries()  # returns a list of dicts or a DataFrame
            if isinstance(queries, pd.DataFrame):
                df = queries
            else:
                df = pd.DataFrame(queries)
        except Exception as e:
            st.error(f"Failed to load queries from database: {e}")
            return

        if df.empty:
            st.info("No queries found in the database.")
            return

        # ----- Search and Filter -----
        st.subheader("Search & Filter Queries")
        col1, col2 = st.columns([2, 1])

        with col1:
            search_term = st.text_input("Search by Client Name or Email").lower()

        with col2:
            # Always show all possible statuses
            all_statuses = ["Open", "Closed"]
            status_filter = st.selectbox("Filter by Status", ["All"] + all_statuses)

        filtered_df = df.copy()

        # Filter by search term
        if search_term:
            filtered_df = filtered_df[
                filtered_df["client_name"].str.lower().str.contains(search_term) |
                filtered_df["email"].str.lower().str.contains(search_term)
            ]

        # Filter by status
        if status_filter != "All":
            filtered_df = filtered_df[filtered_df["status"] == status_filter]

        # ----- Editable DataFrame -----
        # st.markdown("### Editable Query Table")
        st.info("You can directly edit fields such as **Status**, **Description**, etc.")

        edited_df = st.data_editor(
            filtered_df,
            num_rows="fixed",  # prevents adding/removing rows
            use_container_width=True,
            key="editable_table",
             column_config={
                "Status": st.column_config.SelectboxColumn(
                    "Status", options=["Open", "Closed"], help="Change query status"
                )
            }
        )

        st.markdown("---")
        if st.button(" Save Changes"):
            try:
                # Update database with edited data
                query_services.update_queries(edited_df)
                st.success(" Changes saved successfully.")
                refreshed_data = query_services.get_all_queries()
                refreshed_df = pd.DataFrame(refreshed_data)
                # st.rerun()
            except Exception as e:
                st.error(f"Failed to save changes: {e}")

    elif page == "Logout":
        st.session_state.logged_in = False
        st.session_state.role = None
        st.session_state.email = None
        st.session_state.view = "login"
        st.rerun()
