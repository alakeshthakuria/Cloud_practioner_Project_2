from flask import Flask, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db_config = {
    'host': '<PRIVATE_IP_OF_MYSQL_VM>',
    'user': 'frontend_user',
    'password': 'StrongPassword123!',
    'database': 'user_data'
}

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    try:
        # Connect to MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert data
        query = "INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, phone))
        conn.commit()

        return redirect('/?success=1')  # Redirect to the form with success

    except Exception as e:
        return f"Error: {str(e)}", 500

    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run on port 5000
