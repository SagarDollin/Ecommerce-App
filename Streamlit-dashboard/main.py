import streamlit as st
from login import render_login
from product_catalogue import render_product_catalogue
from profile import render_profile
from streamlit_elements import elements, mui, html, sync
from login import navigate_login
from signup import navigate_signup
st.set_page_config(page_title="Data Poem - Assignment", page_icon="assets/logo.jpeg", layout="wide",
                    initial_sidebar_state="collapsed", menu_items=None)
hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = render_login
    # st.session_state.page()


def navigate_profile():
    st.session_state.page = render_profile

def navigate_product_catalogue():
    st.session_state.page = render_product_catalogue

def sidebar():
    with st.sidebar:
        with elements("callbacks_retrieve_data"):
            with elements("style_mui_sx"):
                sx = {
                        "bgcolor": "background.paper",
                        "opacity": 0.7,
                        "minWidth": 280,
                        "boxShadow": 1,
                        "borderRadius": 2,
                        "p": 2,
                        "padding" : 3,
                        "borderLeft": 6,
                        "borderColor": "primary.main",
                        "font-family": "helvetica",
                        "font-color": "white",
                        "textTransform": "none",
                        "color" : "white",
                        'margin': 1,
                        '&:hover': {
                            #'backgroundColor': 'rgba(240, 84, 84, 0.2)',
                            'backgroundColor': 'rgba(41,219,241,0.1)',
                            "borderLeft": 6,
                            "borderColor": "primary.main",
                        }
                }

                mui.Button(
                    "Profile",
                    sx=sx,
                    onClick=navigate_profile
                )                
                
                mui.Button(
                    #"QpiVolta Force",
                    "Product Catalogue",
                    sx=sx,
                    #onClick=navigate_qpiforce
                    onClick=navigate_product_catalogue)
                
                mui.Button(
                    #"QpiVolta Force",
                    "Login",
                    sx=sx,
                    #onClick=navigate_qpiforce
                    onClick=navigate_login)
                
                mui.Button(
                    #"QpiVolta Force",
                    "Signup",
                    sx=sx,
                    #onClick=navigate_qpiforce
                    onClick=navigate_signup)

st.session_state.sidebar = sidebar
st.session_state.sidebar()
st.session_state.page()



