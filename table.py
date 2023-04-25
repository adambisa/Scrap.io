import sqlite3
from myClasses import Url

conn = sqlite3.connect('url_data.db')

c = conn.cursor()

c.execute("""
          CREATE TABLE IF NOT EXISTS urls (
              id text,
              url text,
              price text,
              email text,
              timestamp integer
          )
          """)


def add_url(url):
    conn = sqlite3.connect('url_data.db')

    c = conn.cursor()

    c.execute('INSERT INTO urls VALUES (:id, :url,:price,:email, :timestamp)', {
              'id': url.id, 'url': url.url,'price':url.price,'email':url.email, 'timestamp': url.timestamp})

    conn.commit()
    conn.close()


def view_urls():
    conn = sqlite3.connect('url_data.db')

    c = conn.cursor()

    c.execute('SELECT * FROM urls')
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete_url(url):
    conn = sqlite3.connect('url_data.db')

    c = conn.cursor()

    c.execute('DELETE FROM urls WHERE id = :id ', {'id': url.id})
    conn.commit()
    conn.close()
