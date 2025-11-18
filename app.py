from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def base():
    return render_template("base.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
