#department Select
@app.route('/department', methods=['POST'])
def get_departments():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_department;")
    res = []
    for row in cursor:
        res.append(row)
    return jsonify(res)

#department Insert
@app.route('/department/add', methods=['POST'])
def add_departments():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Insert_department("+json["departmentName"]+");")
    mysqldb.commit()
    return 'success'

#department Update
@app.route('/department/update', methods=['POST'])
def update_departments():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Update_department("+str(json["departmentID"])+","+json["departmentName"]+");")
    mysqldb.commit()
    return 'success'

#department Delete
@app.route('/department/delete', methods=['POST'])
def delete_departments():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Delete_department("+str(json['departmentName'])+");")
    mysqldb.commit()
    return 'success'
