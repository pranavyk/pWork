from app import app
from flask import render_template


@app.route('/')
@app.route('/ydk')
def index():
    user = {'username': 'Pranav'}
    posts = [
        {
            'author': {'username': 'Susan'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, items=['Item1', 'Item2'], posts=posts)

