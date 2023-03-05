import streamlit as st
import pandas as pd
import numpy as np
import uuid
from streamlit_chat import message, AvatarStyle
import streamlit_chat
import openai
st.set_page_config(
    page_title="myGPT",
    page_icon=":sparkles:",
    initial_sidebar_state="expanded"
)
st.header("Welcome to myGPT")
st.markdown("Made with love by Kelvin Wong. :blue_heart:")
st.markdown(" - Follow me on Instagram @<a href = 'https://www.instagram.com/wongkingwang/'>wongkingwang</a>.",unsafe_allow_html=True)
st.markdown(" - Find me @<a href = 'https://www.linkedin.com/in/kelvinwonghkust/'>linkedln</a>.",unsafe_allow_html=True)
st.markdown("This webpage is still in beta. I will try add more features when I have time.")
st.markdown("<hr>",unsafe_allow_html=True)



openai.api_key = st.secrets["OPENAI_API_KEY"]

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [{
        "message": "Hello, I'm myGPT, your personal assistant.",
        "avatar_style":"big-smile",
        "seed":"Aneka",
        "is_user": False}]
    

def generate_dialogue():
    user_msg = st.session_state.text_input
    st.session_state.chat_history.append(
        {"message":user_msg, "is_user": True,"avatar_style":"adventurer", "key":str(uuid.uuid4())}
    )
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"user" if chat["is_user"] else "system","content": chat["message"]} for chat in st.session_state.chat_history
        ]
    )
    response_msg = completion.choices[0].message.content

    st.session_state.chat_history.append(
        {"message":response_msg, "is_user": False,"avatar_style":"big-smile","seed":"Aneka","key":str(uuid.uuid4())}
    )
    st.session_state.text_input = ""    


with st.expander("Chat history",expanded=True):
    for chat in st.session_state.chat_history:
        message(**chat)

text_input = st.text_input("Your Question", key ='text_input',placeholder="Type something", on_change=generate_dialogue)



# Side bar session
with st.sidebar:
    st.title("Welcome to myGPT!:balloon:")
    st.subheader    ("What is myGPT?")
    st.caption('''
    myGPT is a project created by me,
    aiming to create an interesting chatting experience
    for everyone, like you.''')
    st.caption("myGPT is built on gpt-3.5-turbo, the lastest language model developed by OpenAI.")
    st.caption('''
    If you want to know more about OpenAI, or chatGPT in general, click <a href = 'https://openai.com/'>here</a>
    ''',unsafe_allow_html=True)
