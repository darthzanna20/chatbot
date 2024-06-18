from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)
CORS(app)

# Sample data for demonstration
corpus = [
    "Hi",
    'What is the weather today?',
    'Can you tell me a joke?',
    'How do I create an account?',
    'Thank you for your assistance.',
    "What time does the store close?",
    "How can I change my password?",
    "Where is your office located?",
    "I'm having issues with my order. Can you help?",
    "How do I deactivate my account?",
    "Do you offer discounts?",
    "How can I speak with a representative?",
    "What forms of payment do you take?",
    "Can I update my contact information?",
    "How do I change my profile picture?",
    "Is there a desktop application available?",
    "How can I stop receiving notifications?",
    "Where can I view my transaction history?",
    "Where can I find your privacy policy?",
    "What should I do if I forget my PIN?",
    "How do I remove my account?",
    "Is my information safe with you?",
    "How can I upgrade my membership?",
    "What should I do if I find an error?"
]

def respond(intent_index):
    # Responses corresponding to intents
    responses = [
        "Hi! How are you?",
        "The weather is sunny today.",
        "Why don't scientists trust atoms? Because they make up everything!",
        "You can create an account by visiting our sign-up page.",
        "You're very welcome!",
        "The store closes at 9 PM.",
        "You can change your password in your account settings.",
        "Our office is located at 123 Main Street.",
        "Please provide your order number, and we will assist you.",
        "You can deactivate your account in your account settings.",
        "Yes, we offer various discounts throughout the year.",
        "You can speak with a representative by calling our support number.",
        "We accept credit cards, debit cards, and PayPal.",
        "You can update your contact information in your profile settings.",
        "To change your profile picture, go to your profile settings and upload a new image.",
        "Yes, we have a desktop application available for download on our website.",
        "You can stop receiving notifications in your notification settings.",
        "You can view your transaction history in your account dashboard.",
        "You can find our privacy policy on our website.",
        "If you forget your PIN, please contact our support team.",
        "You can remove your account in your account settings.",
        "Yes, your information is safe with us. We use advanced encryption.",
        "You can upgrade your membership in your account settings.",
        "If you find an error, please report it to our support team with details."
    ]

    # Adjust responses based on entities or additional logic if needed
    response = responses[intent_index]
    return response

# Tokenization and preprocessing
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_vectors = tfidf_vectorizer.fit_transform(corpus)

def get_intent(query):
    # Tokenize the input query
    words = nltk.word_tokenize(query)

    # Calculate TF-IDF vectors
    query_vector = tfidf_vectorizer.transform([query])

    # Calculate similarities with each document
    similarities = cosine_similarity(query_vector, tfidf_vectors)

    # Get the index of the most similar document
    most_similar_index = np.argmax(similarities)

    return most_similar_index

@app.route('/messages', methods=['POST', 'OPTIONS'])
def chatbot():
    if request.method == 'OPTIONS':
        # Handle CORS preflight request
        return '', 204

    data = request.get_json()

    if 'user_input' not in data:
        return jsonify({'error': 'Missing user_input field'}), 400

    user_input = data['user_input']

    # Perform intent classification and response generation here

    return jsonify({'response': respond(get_intent(user_input))})

if __name__ == '__main__':
    app.run(debug=True)
