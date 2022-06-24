import finalapp
import form
import streamlit as st

st.set_page_config(
    page_title="Discord Bot",
    page_icon="🐾")

# Pages as key-value pairs
PAGES = {
    "Dashboard": finalapp,
    "Custom Message Creation": form
}

st.sidebar.title('Go to:')

selection = st.sidebar.radio("", list(PAGES.keys()))

page = PAGES[selection]

page.app()
