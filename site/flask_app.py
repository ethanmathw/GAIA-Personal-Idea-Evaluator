from flask import Flask, render_template, request
from openai_helper import get_openai_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        problem_text = request.form['problem']
        solution_text = request.form['solution']

        # Call OpenAI API to get the response
        openai_response = get_openai_response(problem_text, solution_text)

        # Parse OpenAI response
        # You need to implement your own logic to extract values from the OpenAI response
        # and convert them into a format suitable for your result dictionary.

        result = openai_response

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

