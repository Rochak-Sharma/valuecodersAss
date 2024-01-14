from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import os

app = Flask(__name__)

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            processed_data = process_text_data(file_path)
            visualization = generate_visualization(processed_data)
            return jsonify(visualization)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

def process_text_data(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    blob = TextBlob(text)
    sia = SentimentIntensityAnalyzer()
    nltk_sentiment = sia.polarity_scores(text)
    return {
        'polarity': blob.sentiment.polarity,
        'subjectivity': blob.sentiment.subjectivity,
        'nltk_sentiment': nltk_sentiment
    }

def generate_visualization(processed_data):
    visualization_data = {
        'textblob_polarity': processed_data['polarity'],
        'textblob_subjectivity': processed_data['subjectivity'],
        'nltk_sentiment': processed_data['nltk_sentiment']
    }
    return visualization_data

if __name__ == '__main__':
    app.run(debug=True)
