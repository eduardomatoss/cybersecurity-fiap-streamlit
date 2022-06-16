import streamlit as st


from app.view.components import PAGES
from app.cache.cache import load_widget_state


def create():
    load_widget_state()
    PAGES[st.session_state.page]()
