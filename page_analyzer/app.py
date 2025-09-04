import psycopg2
import os
import validators
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request , flash, redirect , url_for
from psycopg2.extras import RealDictCursor
from datetime import datetime
from page_analyzer.parse import parser_h1, parser_title, parser_description


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


DATABASE_URL = os.getenv('DATABASE_URL')

def get_connection():
    return psycopg2.connect(DATABASE_URL)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/urls')
def urls():
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as curs:
            curs.execute('''
    SELECT 
        u.id,
        u.name,
        u.created_at,
        latest.created_at as last_check,
        latest.status_code as last_check_status
    FROM urls u
    LEFT JOIN (
        SELECT DISTINCT ON (url_id)
            url_id,
            status_code,
            created_at
        FROM url_checks
        ORDER BY url_id, created_at DESC
    ) latest ON u.id = latest.url_id
    ORDER BY u.created_at DESC;
''')
            result = curs.fetchall()
    return render_template('urls.html', urls=result)


@app.route('/urls' , methods=['post'])
def urls_add():
    urls = request.form.get('url')
    if not validators.url(urls):
        flash('Некорректный URL', 'danger')
        return render_template('index.html'), 422

    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as curs:
            curs.execute('SELECT id from urls WHERE name =%s;',(urls,))
            result = curs.fetchone()
            if result:
                flash('Страница уже существует', 'info')
                return  redirect(url_for('show_url', id=result['id']))
            curs.execute('INSERT INTO urls (name, created_at)'
                         'VALUES (%s,%s) RETURNING id;',
                         (urls,datetime.now()))
            url_id = curs.fetchone()['id']
            conn.commit()
            flash('Страница успешно добавлена', 'success')
            return redirect(url_for('show_url', id=url_id))


@app.route('/urls/<int:id>')
def show_url(id):
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as curs:
            curs.execute('SELECT id , name , created_at FROM urls WHERE id =%s', (id,))
            url = curs.fetchone()
            curs.execute('SELECT id, url_id, status_code, h1, title, description, created_at FROM url_checks WHERE url_id =%s ORDER BY created_at DESC', (id,))
            check = curs.fetchall()
    return  render_template('urls_show.html', show=url, checks=check)


@app.route('/urls/<int:id>/checks', methods=['post'])
def add_check(id):
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as curs:
            curs.execute('SELECT id, name FROM urls WHERE id =%s', (id,))
            url_data = curs.fetchone()
            url_name = requests.get(url_data['name'])
            if not url_data:
                flash('Сайт не найден', 'danger')
                return redirect(url_for('urls'))
            try:
                status_code = requests.get(url_data['name'])
                status_code.raise_for_status()
            except requests.RequestException:
                flash("Произошла ошибка при проверке", "danger")
                return redirect(url_for("show_url", id=id))
            h1 = parser_h1(url_name)
            title = parser_title(url_name)
            description = parser_description(url_name)
            with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO url_checks (url_id, status_code, h1,
                                                title, description, created_at)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        """,
                        (id, status_code.status_code, h1, title, description,
                         datetime.now())
                    )
                    conn.commit()
            flash('Cтраница успешно проверенна', 'success')
    return redirect(url_for('show_url', id=id))








