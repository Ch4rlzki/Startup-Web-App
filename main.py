import streamlit as st
from streamlit_option_menu import option_menu
from rules.py import rulesBisaya, rulesEnglish

with st.sidebar:
    selected = option_menu(
        "Menu", 
        [
            "Rules",
        ], 
        icons=[
            'check-circle-fill', 
        ], menu_icon="list", default_index=0
    )

if selected == "Rules":
    
    rulesBisaya()