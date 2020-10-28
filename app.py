from flask import Flask, render_template, request, jsonify
from query import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/result', methods=['POST'])
def result():
    """"""
    regex = request.form['regex']
    test_str = request.form['test_str']
    matches, indices = rgx_qu(regex, test_str)
    return render_template('result.html', regex=regex, matches=matches, indices=indices, test_str=test_str)


if __name__ == "__main__":
    app.run(debug=True)
