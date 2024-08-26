from flask import Flask, request, jsonify, render_template
import ollama

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_input = data['message']
    print("User Input:", user_input)  # Print user input on the terminal

    response = ollama.chat(model='deepseek-coder:1.3b', messages=[
        {
            'role': 'user',
            'content': user_input,
        },
    ])
    model_response = response['message']['content']
    print("Model Response:", model_response)  # Print model response on the terminal

    return jsonify({'model_response': model_response})  # Wrap response in a dictionary

if __name__ == '__main__':
    app.run(debug=True)
