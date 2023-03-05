import streamlit as st
import pandas as pd
import numpy as np
import uuid
from streamlit_chat import message
import streamlit_chat
import openai
st.set_page_config(
    page_title="myGPT",
    page_icon=":sparkles:",
    initial_sidebar_state="expanded"
)

st.markdown("Made with love by Kelvin Wong. :blue_heart:")
st.markdown(" - Follow me at Instagram @wongkingwang")
st.markdown(" - Find me @<a href = 'https://www.linkedin.com/in/kelvinwonghkust/'>linkedln</a>",unsafe_allow_html=True)
st.markdown("<hr>",unsafe_allow_html=True)

openai.api_key = st.secrets["OPENAI_API_KEY"]

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [{
        "message": "Hello, my name is king, your personal assistant.",
        "is_user": False}]
    st.session_state['counter'] = 1


def generate_dialogue():
    user_msg = st.session_state.text_input
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_msg}
        ]
    )
    response_msg = completion.choices[0].message.content
    st.session_state.chat_history.append(
        {"message":user_msg, "is_user": True, "key":str(uuid.uuid4())}
    )
    st.session_state.chat_history.append(
        {"message":response_msg, "is_user": False,"key":str(uuid.uuid4())}
    )
    st.session_state.text_input = ""    



for chat in st.session_state.chat_history:
    message(**chat)

text_input = st.text_input("Your Question", key ='text_input',placeholder="Type something", on_change=generate_dialogue)



# Side bar session
with st.sidebar:
    st.title("Welcome to myGPT!:balloon:")
    st.markdown("What is myGPT?")
    st.markdown('''
    myGPT is a project created by me,
    aiming to create an interesting chatting experience
    for everyone, like you.''')
    st.markdown("myGPT is built upon gpt-3.5-turbo, the lastest language model developed by OpenAI.")
    st.write('''
    If you want to know more about OpenAI, or chatGPT in general, click <a href = 'https://openai.com/'>here</a>
    ''',unsafe_allow_html=True)