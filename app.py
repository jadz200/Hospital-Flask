from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin123@localhost:3306/exchange'
mysql = MySQL(app)


@app.route('/departement', methods=['GET'])
def list_department():
    json = request.json
    cur = mysql.connection.cursor()
    cur.execute("SELECT departmentID, departmentName FROM Hospital.department")
    mysql.connection.commit()
    cur.close()
    return 'success'