import string
import random
import streamlit as st

def generaPassword():
    password = ''
    for i in range (10):
        password += random.choice(string.ascii_letters)
    return password

st.set_page_config(page_title="Generatore di password", page_icon="🔐",layout="centered", initial_sidebar_state="expanded")

gradient_text_html="""
    <style>
        .title {
            background: linear-gradient(45deg, #14a0eb, #1c60e3);
            background-clip: text;
            -webkit-background-clip: text;
            color: transparent;
            text-align: center;
        }
    </style>

    <style>
        .paragraph {
            font: 50px, bold;
            text-align: center;
            backlground-color: #ffff
        }
    </style>
    <h1 class="title">Generatore di password</h1>
    <p class="paragraph">Clicca il bottone per generare una password casuale</p>
"""

st.markdown(gradient_text_html, unsafe_allow_html=True)
    

if st.button("Genera password"):
    passwords = generaPassword()
    password_html = f"""
    <div style="
        border:2px solid #14a0eb;
        border-radius:5px;
        padding:10px;
        color:#14a0eb;
        font-weight:bold;
        font-size:20px;
        text-align:center;
        background-color:#0000;
        ">
        <strong>{passwords}</strong>
    </div>
    """
    st.markdown(password_html, unsafe_allow_html=True)