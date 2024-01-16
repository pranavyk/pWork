from app import app
from flask import render_template


@app.route('/')
@app.route('/ydk')
def index():
    user = {'username': 'Pranav'}
    return render_template('index.html', title='Home', user=user, items=['Item1', 'Item2'])

