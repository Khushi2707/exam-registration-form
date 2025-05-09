from flask import Flask, request, render_template
import mysql.connector
from db_config import db_config  # Import database configuration

app = Flask(__name__)

# Route to render the form
@app.route('/')
def index():
    return render_template('form.html')

# Route to handle form submission and insert data into MySQL
@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    name = request.form['name']
    roll = request.form['roll']
    subject = request.form['subject']

    # Connect to MySQL database using db_config
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Insert form data into the registration table
    cursor.execute("INSERT INTO registration (name, roll, subject) VALUES (%s, %s, %s)", (name, roll, subject))

    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()

    return f"Registration submitted for {name}!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
