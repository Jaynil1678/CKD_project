# CKD_project

# Chronic Kidney Disease (CKD) Prediction

A web application that predicts the risk of Chronic Kidney Disease based on a user's health metrics. This tool is designed to provide an accessible and preliminary assessment for informational purposes and to promote early health awareness.

-----

### Project Features

  * *Web Interface:* A user-friendly and responsive web form built with HTML and Flask for easy data input.
  * *Machine Learning Model:* A robust *Logistic Regression model* trained to predict the likelihood of CKD.
  * *Data Handling:* The model is trained on a cleaned dataset, with class imbalance addressed using *SMOTE (Synthetic Minority Over-sampling Technique)* to ensure accurate predictions for the minority class.
  * *Deployment-Ready:* The model is saved as a serialized .pkl file, making it easy to deploy within a web framework like Flask.

-----

### Technologies Used

  * *Python:* The core programming language for the backend and data science.
  * *Flask:* A lightweight web framework used to build the web application.
  * *Pandas:* For data cleaning, preprocessing, and manipulation.
  * *scikit-learn:* For building and training the Logistic Regression model.
  * *imbalanced-learn:* To handle the class imbalance in the dataset using SMOTE.
  * *HTML/CSS:* For the front-end user interface.

-----

### Setup and Installation

Follow these steps to get a copy of the project up and running on your local machine.

#### Prerequisites

  * Python 3.8+
  * pip (Python package installer)

#### 1\. Clone the repository

bash
git clone [repository_url]
cd [repository_name]


#### 2\. Install dependencies

It is recommended to use a virtual environment.

bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
pip install -r requirements.txt


**requirements.txt content:**


Flask
pandas
numpy
scikit-learn
imbalanced-learn


#### 3\. Train the model

To ensure you have a working model file (CKD.pkl), run the training script. This script will perform data preprocessing, apply SMOTE, train the logistic regression model, and save it to a file.

bash
python train_model.py


#### 4\. Run the Flask application

With the model file in place, you can now start the web server.

bash
python app.py


The application will be accessible at http://127.0.0.1:5000 in your web browser.

-----

### Important Disclaimer

This CKD prediction tool is for *informational and educational purposes only. The results provided are a probabilistic assessment based on a machine learning model and are **not a substitute for professional medical advice, diagnosis, or treatment*. Always consult with a qualified healthcare professional regarding any medical questions or conditions.

-----

### Future Improvements

  * Improve the user interface with a more modern design and visualizations.
  * Explore additional machine learning models (e.g., Random Forest, Gradient Boosting) to see if performance can be enhanced.
  * Add more detailed explanations about how each feature influences the prediction.
  * Integrate a contact form for user feedback.