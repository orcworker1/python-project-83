import psycopg2
import os
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')


def tes_queries():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT id, name FROM urls WHERE id =2')
    name = cur.fetchone()['name']
    print(name)
    for row in cur.fetchall():
        print(f"ID: {row['id']}, Name: {row['name']}, Created: {row['created_at']}")

tes_queries()

