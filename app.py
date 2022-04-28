from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(user="root",
                              password="E@^KT3Qn!Cf:(}3Y",
                              host="localhost",
                              database="hospital",
                              # use_pure=False
                              )
mysql = MySQL(app)
if (mydb.is_connected()):
    print("Connected")
else:
    print("Not connected")

@app.route('/department', methods=['GET'])
def list_department():
    cur = mydb.cursor()    
    cur.execute("SELECT departmentID, departmentName FROM Hospital.department")
    
    cur.close()
    return 'success'

@app.route('/execute_query', methods=['POST'])
def execute_query():
  
    try:
        print(request.get_json()['query'])
        mydb.execute(request.get_json()['query'])
    except:
        return {"message": "Request could not be completed."}
  
    return {"message": "Query executed successfully."}