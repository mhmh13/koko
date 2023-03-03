from flask import Flask, render_template, request

import openai
openai.api_key = "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"

def process_text(input_text):
    promo = "Ret dette til standard dansk:\n" + input_text
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=promo,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    output_text = response.choices[0].text.strip()
    return output_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input']
        output_text = process_text(input_text)
        return render_template('index.html', output=output_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
