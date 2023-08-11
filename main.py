from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'YOUR_OPEN_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.form.get('question')
    if user_question:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Choose the appropriate engine
            prompt=user_question,
            max_tokens=50
        )
        answer = response.choices[0].text.strip()
    else:
        answer = "Please ask a question."

    return render_template('index.html', question=user_question, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)

