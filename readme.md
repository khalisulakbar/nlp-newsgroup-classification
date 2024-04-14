# Project: NLP - Text Classification

## Introduction
This project focuses on text classification, aiming to train a model to classify textual data from kompas.com articles. The dataset consists of articles published between January 1, 2024, and January 31, 2024, with the article content serving as the feature and the site news being the label. This project aims to classify the site news based on the article content. The model is trained using three algorithms: logistic regression, naive Bayes, and support vector classifier (SVC).


## Tasks
In This Project, I divided the work into three Main Tasks:

### Task 1: Exploratory Data Analysis (EDA)
In Task 1, exploratory data analysis (EDA) was performed to gain insights into the patterns and characteristics of the dataset. I explore statistical measures, visualizations, author analysis, and article characteristics to identify trends, outliers, and areas for further analysis.

### Task 2: Using NLP Models
For Task 2, I apply natural language processing (NLP) techniques and models to preprocess the textual data. Preprocessing includes cleaning HTML tags, punctuation removal, ads removal, tokenization, stop-word removal, and lemmatization to clean the text. Then, an appropriate NLP models are trained, such as logistic regression, naive Bayes, and support vector classifier (SVC) to classify the site news based on the article content. Also, Hyperparameter tuning is performed to improve the performance of the model. Finally, the pipeline of data preprocessing and tuned model is saved as a pickle file.

### Task 3: Building a Simple Interface
In Task 3, a simple web interface is built using Flask and streamlit. The web interface allows users to input textual data and the model predicts the site news based on the article content. the frontend of the web interface is built using streamlit, while the backend is built using Flask. The web interface at the moment is not deployed anywhere yet. However, the web interface is fully functional on localhost.

To run the web interface, go to the terminal and type:
1. git clone this repo.
2. `pip install -r requirements.txt`
3. cd to the directory where the repository is cloned.
4. run machine learning model API: `flask --app /path/to/deployment/backend.py run`
5. run web interface: `streamlit run /path/to/deployment/frontend.py`
6. enter article content in the text box and click the 'Classify' button to classify its category.

## What to do next
1. Deploy the web interface to a production environment/web server.
2. Train the model with more balanced dataset.
3. Tune the model and deploy it to production environment.

## Additional Information
Project: SiteName Classification
