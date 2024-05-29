from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=database-1.c184802yg3ka.af-south-1.rds.amazonaws.com;'
        'DATABASE=Project-Flask-1;'
        'UID=your-admin;'
        'PWD=your-Deutschland1'
    )
    return conn

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Users (Name, Email, Message) VALUES (?, ?, ?)",
        (name, email, message)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)