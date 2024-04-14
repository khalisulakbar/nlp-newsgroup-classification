import streamlit as st
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from preprocess import preprocess_text

# Set page configuration
st.set_page_config(
    page_title="Khalisul_Akbar-Data Scientist",
    page_icon="📰",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/khalisul-akbar/',
        'Report a bug': "https://github.com/khalisulakbar",
        'About': "# NLP proficiency test!!!"
    }
)

# Page Title
st.markdown("<h1 style='text-align: center; color:  #ff957f ;'>Kompas Site News - Text Classification</h1>", unsafe_allow_html=True)
st.markdown("""<hr style="height:10px;border:none;color:#ff957f;background-color:#333;" /> """, unsafe_allow_html=True) 

# Text Classification Web App
st.write("Enter an article in the text box below and click the 'Classify' button to classify its category.")

# Input Text Box
article_text = st.text_area("Enter the article:", "")

# Classify Button
if st.button("Classify"):
    # Make a request to your model endpoint
    model_url = "http://127.0.0.1:5000/predict"
    data = {"Content": article_text}
    try:
        response = requests.post(model_url, json=data)
        if response.status_code == 200:
            result = response.json()

            text = preprocess_text(article_text)
            # Generate and display word cloud
            st.markdown("<h2 style='text-align: center; color:  #ff957f ;'>Word Cloud</h2>", unsafe_allow_html=True)
            wordcloud = WordCloud(width=800, height=400, background_color ='white').generate(text)
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            st.pyplot(plt)

            st.write("Classified Category:",)
            st.markdown(f"<h2 style='text-align: center; color: #ff957f;'>{result['result']['prediction']}</h2>", unsafe_allow_html=True)
        else:
            st.write("Error:", response.text)
    except Exception as e:
        st.write("Error connecting to the model:", e)

st.markdown("""<hr style="height:10px;border:none;color:#ff957f;background-color:#333;" /> """, unsafe_allow_html=True) 