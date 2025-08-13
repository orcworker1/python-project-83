import psycopg2, os , validators
from dotenv import load_dotenv
from flask import Flask, render_template, request , flash

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

load_dotenv()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/urls' , methods=['post'])
def urls_add():
    urls = request.form.get('url')
    if not validators.url(urls):
        flash('Некоректный URL', 'DANGER')
        return render_template('index.html'), 422
    pass
