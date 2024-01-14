# Sentiment Analysis Web Application

This project is a Flask-based web application that allows users to upload text files. It processes the content of the files to perform sentiment analysis using NLTK and TextBlob and visualizes the results.

## Features

- File upload interface
- Sentiment analysis with NLTK VADER and TextBlob
- Visualization of sentiment analysis results
- JSON API response with sentiment analysis data

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python installed on your system. If you do not have Python installed, download and install it from [python.org](https://www.python.org/).

After installing Python, you need to install the required packages:

```bash
pip install flask nltk textblob spacy werkzeug


Additionally, you will need to download the VADER lexicon using NLTK:

python
Copy code
import nltk
nltk.download('vader_lexicon')
Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/your-repository.git
Navigate to the cloned repository:

bash
Copy code
cd your-repository
Start the web application:

bash
Copy code
python app.py
The application will start on http://localhost:5000/ by default.

Usage
To use the application, navigate to http://localhost:5000/ in your web browser. Use the upload form to upload a text file, and then view the sentiment analysis results presented in JSON format.

API Reference
The application provides the following endpoint:

POST /
Uploads a text file and returns the sentiment analysis results in JSON format.
'''bash
