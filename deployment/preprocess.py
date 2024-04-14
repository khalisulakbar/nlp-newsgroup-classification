import re
from bs4 import BeautifulSoup
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import spacy
nlp = spacy.blank("id")
nlp.add_pipe("lemmatizer", config={"mode": "lookup"})
nlp.initialize()

def html_to_text(html):
    # Convert HTML to text using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()


def remove_baca_juga(text):
    # Split the text into lines
    lines = text.split("\n")
    # Remove lines containing "Baca juga"
    cleaned_lines = [line for line in lines if "Baca juga" not in line]
    # Join the cleaned lines back into text
    cleaned_text = "\n".join(cleaned_lines)
    return cleaned_text


def remove_intro_tag(text):
    # Define the regular expression pattern to match the specified format
    pattern = r"\b(?:\w+\,\s+)?KOMPAS\.com\s+\-\s+"
    # Use the re.sub() function to remove the matched pattern and the text before it
    text = re.sub(pattern, "", text)
    return text


def remove_punctuations(text):
    # Define the regular expression pattern to match punctuations
    punct_tag = re.compile(r"[^\w\s]")
    # Use the re.sub() function to remove the punctuations from the text
    text = punct_tag.sub(r"", text)
    return text


def tokenize_text(text):
    # Tokenize the text with NLTK
    tokens = nltk.tokenize.word_tokenize(text)
    return tokens


def remove_stopwords(tokens):
    # Remove stopwords from the tokens with NLTK
    stop_words = set(stopwords.words("indonesian"))
    filtered_tokens = [word for word in tokens if not word in stop_words]
    return filtered_tokens


def lemmatize_text(text):
    # Process the text with spaCy
    doc = nlp(text)
    # Lemmatize each token in the document
    lemmatized_tokens = [token.lemma_ for token in doc]
    return lemmatized_tokens


def remove_duplicates(tokens):
    # Remove duplicates from the tokens
    unique_tokens = []
    for token in tokens:
        if token not in unique_tokens:
            unique_tokens.append(token)
    return unique_tokens


def preprocess_text(text):
    # Preprocess the text using the defined functions
    text = html_to_text(html=text)
    document = remove_baca_juga(text=text)
    document = remove_intro_tag(text=document)
    document = remove_punctuations(text=document)
    tokens = tokenize_text(text=document.lower())
    tokens = remove_stopwords(tokens)

    # Lemmatization
    tokens = lemmatize_text(text=" ".join(tokens))
    return " ".join(tokens)