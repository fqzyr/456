import flask
from flask import url_for

app = flask.Flask(__name__)
@app.route('/')
def index():
    return flask.render_template('index.html')
@app.route('/chose1')
def chose1():
    return flask.render_template('chose1.html')

@app.route('/chose2')
def chose2():
    return flask.render_template('chose2.html')

@app.route('/chose3')
def chose3():
    return flask.render_template('chose3.html')

@app.route('/chose4')
def chose12():
    return flask.render_template('chose4.html')

@app.route('/chose5')
def chose5():
    return flask.render_template('chose5.html')

@app.route('/chose6')
def chose6():
    return flask.render_template('chose6.html')

@app.route('/wrong')
def wrong():
    return flask.render_template('wrong.html')

if __name__ == '__main__':
    app.run(debug=True,port=5200)