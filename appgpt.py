from flask import Flask, request, jsonify, render_template
import openai
import os


app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = open("api.txt", "r").read().strip()  # Store your API key securely

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    # Call OpenAI API for the response
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        
        bot_response = response['choices'][0]['message']['content']
        
        return jsonify({'response': bot_response})
    except openai.error.OpenAIError as e:
        
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
   