from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    conn = mysql.connector.connect(
        host='mysql',
        user='root',
        password='root',
        database='db'
    )
    cursor = conn.cursor()
    cursor.execute('select * from students')
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', students=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
