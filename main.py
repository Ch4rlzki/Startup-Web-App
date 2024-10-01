import streamlit as st
from streamlit_option_menu import option_menu

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
    
    st.title("Pahibalo!")
    st.write("Tungod sa nahitabo nga insidente sa miaging higayon, kami nagdesisyon nga magbutang ug tracker sa matag computer unit. Ang tanan ninyong lihok sa pag-abli ug mga aplikasyon ug pag-browse sa internet amo nang ma-monitor. Kung adunay mosulay nga mopasubra sa among mga balaod, ipatuman ang pag-ban gikan sa paggamit sa computer café.")

    st.header("Mga balaod sa Computer Café:")

    col1, col2 = st.columns(2)
    col2.image("./img/no-smoking.png")
    col1.write("""
    1. Gidili ang pagpanigarilyo o paggamit ug tabako sulod sa computer café.
    """)

    col3, col4 = st.columns(2)
    col3.image("./img/malware.png")
    col4.write("""
    2. Gidili ang pag-download ug mga malisyosong software ug extensions sa computer:
        - Mga halimbawa:
            - Virus
            - Worm
            - Trojan
            - Ransomware
            - Spyware
            - Adware
            - Rootkit
            - Keylogger
    """)

    col5, col6 = st.columns(2)
    col6.image("./img/no-hardware.png")
    col5.write("""
    3. Gidili ang pag-usab o pag-manipula sa mga hardware ug software:
        - Kon adunay guba ang computer, palihug i-report dayon sa amo.
    """)

    col7, col8 = st.columns(2)
    col7.image("./img/cleanliness.png")
    col8.write("""
    4. Paglimpyo ug kaayohan:
        - Ayaw pagbutang ug bisan unsang basura sa sulod sa computer café.
        - Palihug ayuha ug taronga ang bangko human maggamit sa computer.
    """)