import psycopg2, os , validators
from dotenv import load_dotenv
from flask import Flask, render_template, request , flash, redirect , url_for
from psycopg2.extras import RealDictCursor
from datetime import date
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

def get_connection():
    return psycopg2.connect(DATABASE_URL)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/urls')
def show_urls():
    pass


@app.route('/urls' , methods=['post'])
def urls_add():
    urls = request.form.get('url')
    if not validators.url(urls):
        flash('Некорректный URL', 'DANGER')
        return redirect(url_for('index')), 422

    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as curs:
            curs.execute('SELECT id from urls WHERE name =%s;',(urls,))
            result = curs.fetchone()
            if result:
                flash('страница уже существует', 'info')
                return  redirect(url_for(show_urls, id=result['id']))
            curs.execute('INSERT INTO urls (name)'
                         'VALUES (%s) RETURNING id;',
                         (urls,))
            url_id = curs.fetchone()['id']
            conn.commit()
            flash('страница успешно добавлена', 'success')
            return redirect(url_for('urls_show', id=url_id))


#INSERT INTO table_name (column1, column2, ...)
#VALUES (value1, value2, ...);




