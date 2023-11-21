from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h2>Hello, Flask!</h2>"

@app.route("/about")
def about():
    return "<h2>About page</h2>"

if __name__=="__main__":
    app.run(debug=True)