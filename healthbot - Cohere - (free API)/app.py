from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import cohere

app = Flask(__name__)
CORS(app)

co = cohere.Client('')  # Replace with your real API key

# Context memory
conversation_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')

    if not user_message:
        return jsonify({'reply': 'Please enter a message.'})

    # Add user input to chat history
    conversation_history.append({"role": "USER", "message": user_message})

    try:
        response = co.chat(
            chat_history=conversation_history,
            message=user_message,
            model="command-r",  # This model works with chat endpoint
            temperature=0.7
        )

        bot_reply = response.text.strip()

        # Save bot reply
        conversation_history.append({"role": "CHATBOT", "message": bot_reply})

        return jsonify({'reply': bot_reply})
    
    except Exception as e:
        print("❌ Error:", e)
        return jsonify({'reply': 'Sorry, there was an error processing your message.'})

if __name__ == '__main__':
    app.run(debug=True)
