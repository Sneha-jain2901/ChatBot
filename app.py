from flask import Flask, render_template, request, jsonify
from flask import send_from_directory
import requests

app = Flask(__name__, template_folder='tempelate')

# Rasa API URL
RASA_API_URL = 'http://localhost:5005/webhooks/rest/webhook'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/static/<filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    print('User message:', user_message)
    try:
    # Send message to Rasa and get response
        response = requests.post(RASA_API_URL, json={'message': user_message})
        response.raise_for_status()
        rasa_response = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Rasa Server: {e}")
        return jsonify({'error': 'Error coonecting to rasa server'})
    # Extract text response and voice output from Rasa
    bot_response_text = rasa_response[0]['text'] if rasa_response else 'Sorry, I didn\'t understand that.'
    bot_response_voice = rasa_response[0]['voice_output'] if 'voice_output' in rasa_response[0] else None

    print('Bot text response:', bot_response_text)
    print('Bot voice output:', bot_response_voice)

    return jsonify({'text_response': bot_response_text, 'voice_output': bot_response_voice})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
