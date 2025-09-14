import streamlit as st
from home import show_dashboard
from complex_insights import show_profound_insights
from basic_insights import show_fundamental_insights
from add_log import show_add_log

st.set_page_config(
    page_title="Secure Check",
)


selected_page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "💡 Basic Insights", "🧠 Complex Insights", "📝 Add New Police Log"]
)

# Routing Logic
if selected_page == "🏠 Home":
    show_dashboard()
elif selected_page == "💡 Basic Insights":
    show_fundamental_insights()
elif selected_page == "🧠 Complex Insights":
    show_profound_insights()
elif selected_page == "📝 Add New Police Log":
    show_add_log()