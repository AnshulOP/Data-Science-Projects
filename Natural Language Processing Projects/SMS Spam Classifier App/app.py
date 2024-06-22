# Import necessary libraries and modules
from flask import Flask, render_template, request
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize the Flask application
app = Flask(__name__)

# Load the pre-trained model and vectorizer from pickle files
model = pickle.load(open('sms_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))


# Define the home route
@app.route('/')
def home():
    # Render the home page template
    return render_template('index.html')


# Define the predict route to handle POST requests
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the message from the form input
        message = request.form['message']

        # Preprocess the input message
        processed_message = text_preprocessing(message)

        # Vectorize the input using the pre-trained vectorizer
        input_vector = vectorizer.transform([processed_message]).toarray()

        # Make a prediction using the pre-trained model
        prediction = model.predict(input_vector)[0]

        # Determine if the message is spam or not
        if prediction == 1:
            result = 'Spam'
        else:
            result = 'Not Spam'

        # Render the result on the home page template
        return render_template('index.html', prediction_text=f'The message is {result}')


# Function for text preprocessing
def text_preprocessing(text):
    import nltk
    import re
    from nltk.tokenize import word_tokenize
    import string
    from nltk.corpus import stopwords
    from nltk.stem import PorterStemmer

    # Convert text to lowercase
    text = text.lower()

    # Remove HTML tags and URLs using regex
    pattern = re.compile('<.*?>')
    text = pattern.sub(r'', text)

    # Tokenize the text into words
    text = nltk.word_tokenize(text)

    # Initialize the stemmer
    stemmer = PorterStemmer()

    # List to store processed words
    x = []

    # Loop through each word in the text
    for word in text:
        # Remove stopwords and punctuation, then apply stemming
        if word not in stopwords.words('english') and word not in string.punctuation:
            x.append(stemmer.stem(word))

    # Clear the original text list
    text = x[:]
    x.clear()

    # Join the processed words back into a single string
    return " ".join(text)


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
