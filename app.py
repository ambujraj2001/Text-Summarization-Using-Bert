import streamlit as st
import pickle
from PIL import Image



with st.sidebar:
    st.subheader('Text Summarization Using BERT')
    st.divider()
    st.write('This is a text summarization app using BERT. It is a state of the art model for text summarization. It is a pretrained model which is trained on a large dataset of news articles. It can be used for summarizing any text. It is a very powerful model and is very fast. It is also very accurate.')
    image = Image.open('NextSentencePrediction.jpg')
    st.image(image, caption='Bert Model')
    st.code('App Built by Ambuj Raj',language='python')



def summary(txt):
    with st.spinner('Summarizing...'):
        loaded_model = pickle.load(open('bert.sav', 'rb'))
        summary = loaded_model(txt, min_length=50)
    st.success('Your Summary is ready and is given below ⬇️')
    st.subheader(summary)

st.title('Text Summarization Using BERT')
st.divider()
txt = st.text_area('Enter the Text to extract Summary', '''''')
if st.button('Summarize'):
    summary(txt)





