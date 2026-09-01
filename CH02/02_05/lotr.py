from transformers import pipeline
import streamlit as st
st.subheader("A LOTR Fun!")
pipe = pipeline("text-generation",model="TensaZangetsu/condensed-bert-vulnerable",device="cuda")
prompt=st.text_input("Enter your prompt ")
st.write(pipe(prompt)[0]['generated_text'])
