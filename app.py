import os
from flask import Flask, url_for

app = Flask(__name__)
from flask import render_template

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

with app.test_request_context():
 print url_for('static', filename='mystyle.css')



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)