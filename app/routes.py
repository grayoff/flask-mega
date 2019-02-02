from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Grayoff'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day today!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Movie was so cool!'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
