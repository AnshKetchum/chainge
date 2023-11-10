import streamlit as st
from langchain.llms import OpenAI
from chainge.config import OPENAI_API_KEY
import openai 

openai.version = "1.2.0"


st.title('🦜🔗 Quickstart App')


def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=OPENAI_API_KEY)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if submitted:
    generate_response(text)