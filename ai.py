from flask import Flask, request, jsonify
import google.generativeai as genai

# Configure Google Gemini API
genai.configure(api_key="AIzaSyAyLpOSQK73S0T5h3eUY9CqWmSm2Hs53N0")
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize the Flask app
app = Flask(__name__)

# Create a chat session
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello, I need help managing my finances."},
        {"role": "model", "parts": "Sure! I'd be happy to help. What financial advice are you looking for? Budgeting, saving, or investing?"}
    ]
)

# Store user financial profile
user_profile = {
    "income": None,
    "expenses": None,
    "savings": None,
    "debt": None,
    "goals": []
}

# API endpoint to interact with the chatbot
@app.route('/chat', methods=['POST'])
def chat_with_bot():
    user_input = request.json.get('message')  # Get the user's message
    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    # Process financial advice based on input
    if "income" in user_input.lower():
        user_profile["income"] = request.json.get('income', "Not provided")
    elif "expenses" in user_input.lower():
        user_profile["expenses"] = request.json.get('expenses', "Not provided")
    elif "savings" in user_input.lower():
        user_profile["savings"] = request.json.get('savings', "Not provided")
    elif "debt" in user_input.lower():
        user_profile["debt"] = request.json.get('debt', "Not provided")

    # Get the response from the chatbot
    response = chat.send_message(user_input)
    chat.history.append({"role": "user", "parts": user_input})
    chat.history.append({"role": "model", "parts": response.text})
    
    # Return the response
    return jsonify({"response": response.text})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)