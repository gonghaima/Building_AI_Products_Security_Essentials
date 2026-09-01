from transformers import pipeline
import streamlit as st
st.subheading("Manastas Sentence Predictor")
pipe=pipeline("text-generation",model="manastas/vulnerable_model")
prompt=st.text_input("Enter your prompt")
st.write(pipe(prompt)[0]['generated_text']
