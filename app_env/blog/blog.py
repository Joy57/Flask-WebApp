from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author':'Joy abe',
        'title' :'Post 1',
        'content': 'First content 1',
        'date_posted':'May 18, 2018'
    },
    {
        'author':'Sample Guy',
        'title' :'Post 2',
        'content': 'First content 2',
        'date_posted':'May 18, 2018'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About Page')

if __name__ == '__main__':
    app.run(debug=True)