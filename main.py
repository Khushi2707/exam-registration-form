from flask import Flask, request, render_template
import mysql.connector
from db_config import db_config

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    roll = request.form['roll']
    subject = request.form['subject']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO registration (name, roll, subject) VALUES (%s, %s, %s)", (name, roll, subject))
    conn.commit()
    cursor.close()
    conn.close()
    return f"Registration submitted for {name}!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
