from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return redirect(url_for('static_sample'))

@app.route('/viewer')
def static_sample():
    return render_template("static.html")

if __name__ == '__main__':
    app.run()
