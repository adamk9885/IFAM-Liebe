import streamlit as st
def page_setup():
    st.set_page_config(layout="wide")
    st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")  # hide links next to headers
    st.markdown('''<style>button[title="View fullscreen"]{visibility: hidden;}</style>''',
                unsafe_allow_html=True)  # hide full screen image option

    col1, col2, col3 = st.columns([3.5, 4, 3])
    with col2:
        st.image("IFAM_logo.png")

    st.markdown(f"""<div style="height: 50px;"></div>""", unsafe_allow_html=True)