import streamlit as st
import pickle as pk

tfidf=pk.load(open('vectorizer.pkl','rb'))
model=pk.load(open('model.pkl','rb'))

st.title("EMAIL/SMS SPAM CLASSIFIER")

input_sms=st.text_input("Enter the message")

