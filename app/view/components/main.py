import streamlit as st


from app.view.components import components
from app.cache.cache import load_widget_state

def create():
    load_widget_state()
    components.PAGES[st.session_state.page]()