from flask import Flask, render_template, request
import sqlite3


app = Flask('blog-app', template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index_post():
    conn = sqlite3.connect('blogs.db')
    c = conn.cursor()
    try:
        c.execute("""CREATE TABLE bloggers (first text, last text, post text)""")
    except sqlite3.OperationalError:
        pass
    firstname_text = request.form['firstname']
    lastname_text = request.form['lastname']
    post_text = request.form['post_text']
    params = (firstname_text, lastname_text, post_text)
    c.execute(f"INSERT INTO bloggers VALUES (?, ?, ?)", params)
    conn.commit()
    conn.close()
    return 'Your post has been saved successfully'


app.run()
