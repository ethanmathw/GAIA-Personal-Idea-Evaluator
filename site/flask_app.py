from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        problem_text = request.form['problem']
        solution_text = request.form['solution']

        result = {
            'evaluation': {
                'economic_stability': 8,
                'technological_innovation': 7,
                'feasibility': 9,
                'circular_economy': 8
            },
            'feedback': 'Your focus on solar power is commendable, showing good economic stability and technological innovation. However, consider exploring circular economy principles for more sustainable solutions.',
            'problem_text': problem_text,
            'solution_text': solution_text
        }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

