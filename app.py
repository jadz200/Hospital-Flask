from colorama import Cursor
from flask import Flask,render_template, request,jsonify
import mysql.connector  as mysql

app = Flask(__name__)
 

mysqldb =mysql.connect(host="127.0.0.1",user="root",password="admin",database="hospital")



#Patients Select
@app.route('/patient', methods=['POST'])
def get_patient():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_patient;")
    res = []
    for row in cursor:
        res.append(row)
    return jsonify(res)

#Patients Insert
@app.route('/patient/add', methods=['POST'])
def add_patient():
    cursor=mysqldb.cursor()

    json = request.json
    cursor.execute("call hospital.Insert_Patient(%s, %s, %s, %s);", (json['fname'], json['lname'], json['email'], json['phone']))
    mysqldb.commit()
    return 'success'

#Patients Update
@app.route('/patient/update', methods=['POST'])
def update_patient():
    cursor=mysqldb.cursor()

    json = request.json
    cursor.execute("call hospital.Update_Patient("+str(json['patientID'])+",%s, %s, %s, %s);", (json['fname'], json['lname'], json['email'], json['phone']))
    mysqldb.commit()
    return 'success'
#Patients Delete

@app.route('/patient/delete', methods=['POST'])
def delete_patient():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Delete_Patient("+str(json['PatientID'])+");")
    mysqldb.commit()
    return 'success'

#Staff Select
@app.route('/staff', methods=['POST'])
def get_staffs():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_staff;")
    res = []
    for row in cursor:
        res.append(row)
    return jsonify(res)


#Staff Insert
@app.route('/staff/add', methods=['POST'])
def add_staff():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Insert_staff("+str(json['departmentID']) +",%s, %s, %s, %s);", (json['fname'], json['lname'], json['email'], json['phone']))
    mysqldb.commit()
    return 'success'

#Staff Update
@app.route('/staff/update', methods=['POST'])
def update_staff():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Update_staff("+str(json['StaffID'])+","+str(json['departmentID']) +",%s, %s, %s, %s);", (json['fname'], json['lname'], json['email'], json['phone']))
    mysqldb.commit()
    return 'success'
#Staff Delete
@app.route('/staff/delete', methods=['POST'])
def delete_staff():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Delete_Staff("+str(json['StaffID'])+");")
    mysqldb.commit()
    return 'success'



#Manager Select
@app.route('/manager', methods=['POST'])
def get_managers():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_manager;")
    res = []
    for row in cursor:
        res.append(row)
    return jsonify(res)

#Manager Insert
@app.route('/manager/add', methods=['POST'])
def add_managers():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Insert_Manager("+str(json['ManagerID'])+","+str(json['departmentID'])+");")
    mysqldb.commit()
    return 'success'

#Manager Update
@app.route('/manager/update', methods=['POST'])
def update_managers():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Update_Manager("+str(json['ManagerID'])+","+str(json['departmentID'])+");")
    mysqldb.commit()
    return 'success'

#Manager Delete
@app.route('/manager/delete', methods=['POST'])
def delete_managers():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Delete_Manager("+str(json['ManagerID'])+");")
    mysqldb.commit()
    return 'success'

#MedicalStaff Select
@app.route('/medicalstaff', methods=['POST'])
def get_MedicalStaffs():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_MedicalStaff;")
    res = []
    for row in cursor:
        res.append(row)
    return jsonify(res)

#MedicalStaff Insert
@app.route('/medicalstaff/add', methods=['POST'])
def add_MedicalStaffs():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Insert_MedicalStaff("+str(json['MedStaffID'])+","+str(json['scheduleID'])+");")
    mysqldb.commit()
    return 'success'

#MedicalStaff Update
@app.route('/medicalstaff/update', methods=['POST'])
def update_MedicalStaffs():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Update_MedicalStaff("+str(json['MedStaffID'])+","+str(json['scheduleID'])+");")
    mysqldb.commit()
    return 'success'

#MedicalStaff Delete
@app.route('/medicalstaff/delete', methods=['POST'])
def delete_MedicalStaffs():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Delete_MedicalStaff("+str(json['MedStaffID'])+");")
    mysqldb.commit()
    return 'success'



#secretary Select
@app.route('/secretary', methods=['POST'])
def get_secretarys():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_secretary;")
    res = []
    for row in cursor:
        res.append(row)
    return jsonify(res)

#secretary Insert
@app.route('/secretary/add', methods=['POST'])
def add_secretarys():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Insert_secretary("+str(json['secretaryID'])+");")
    mysqldb.commit()
    return 'success'

#No Update for secretary

#secretary Delete
@app.route('/secretary/delete', methods=['POST'])
def delete_secretarys():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Delete_secretary("+str(json['secretaryID'])+");")
    mysqldb.commit()
    return 'success'

#medicine Select
@app.route('/medicine', methods=['POST'])
def get_medicines():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_medecine;")
    res = []
    for row in cursor:
        res.append(row)
    return jsonify(res)

#medicine Insert
@app.route('/medicine/add', methods=['POST'])
def add_medicines():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Insert_Medicine("+json["medname"]+","+str(json["inventory"])+", "+json["meddescription"]+");")
    mysqldb.commit()
    return 'success'

#medicine Update
@app.route('/medicine/update', methods=['POST'])
def update_medicines():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Update_Medicine("+str(json["MedicineID"])+","+json["medname"]+","+str(json["inventory"])+", "+json["meddescription"]+");")
    mysqldb.commit()
    return 'success'
#medicine Delete
@app.route('/medicine/delete', methods=['POST'])
def delete_medicines():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Delete_medicine("+str(json['medicineID'])+");")
    mysqldb.commit()
    return 'success'









@app.route('/appointments', methods=['POST'])
def get_appointments():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_appointment;")
    res = []
    for row in cursor:
        res.append(row)
    return jsonify(res)




 
