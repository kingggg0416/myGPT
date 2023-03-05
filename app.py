import streamlit as st
import pandas as pd
import numpy as np
import uuid
from streamlit_chat import message
import streamlit_chat
import openai

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

text_input = st.text_input("Your Question", key ='text_input', on_change=generate_dialogue)
