import streamlit as st
import pickle as pk

def transform_text(text):
    text=text.lower()
    text=nltk.word_tokenize(text)

    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)

    text=y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text=y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)



tfidf=pk.load(open('vectorizer.pkl','rb'))
model=pk.load(open('model.pkl','rb'))

st.title("EMAIL/SMS SPAM CLASSIFIER")

input_sms=st.text_input("Enter the message")

#preprocess
transform_sms=transform_text(input_sms)

