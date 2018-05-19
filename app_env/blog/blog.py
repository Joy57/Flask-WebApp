from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return "<h1>Hello World!<h1>\n"


@app.route("/about")
def about():
    return "<h1>about page!<h1>\n"

if __name__ == '__main__':
    app.run(debug=True)