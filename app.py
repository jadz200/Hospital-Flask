from colorama import Cursor
from flask import redirect, render_template, request, Flask, jsonify
import mysql.connector  as mysql

app = Flask(__name__)
 
app.run(host='localhost', port=5000)

mysqldb =mysql.connect(host="127.0.0.1",user="root",password="admin",database="hospital")

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')
#Patients Select
@app.route('/patient', methods=['GET','POST'])
def get_patient():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_patient;")
    res = []
    for row in cursor:
        res.append(row)
    return render_template('patient/patient.html',patients=res)

#Patients Insert
@app.route('/patient/add', methods=['GET','POST'])
def add_patient():
    if request.method == 'GET':
        return render_template('patient/patient_add.html')
 
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Insert_Patient(%s, %s, %s, %s);", (fname, lname, email, phone))
        mysqldb.commit()
        return redirect('/patient')

#Patients Update
@app.route('/patient/update', methods=['GET','POST'])
def update_patient():
    if request.method == 'GET':
        return render_template('patient/patient_update.html')
 
    if request.method == 'POST':
        patientID = request.form.get('patientID')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Update_Patient("+patientID+",%s, %s, %s, %s);", (fname,lname,email,phone))
        mysqldb.commit()
        return redirect('/patient')
#Patients Delete

@app.route('/patient/delete', methods=['GET','POST'])
def delete_patient():
    if request.method == 'GET':
        return render_template('patient/patient_delete.html')
 
    if request.method == 'POST':
        patientID = request.form.get('patientID')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Delete_Patient("+patientID+");")
        mysqldb.commit()
        return redirect('/patient')


#Staff Select
@app.route('/staff', methods=['GET','POST'])
def get_staffs():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_staff;")
    res = []
    for row in cursor:
        res.append(row)
    return render_template('staff/staff.html',staffs=res)


#Staff Insert
@app.route('/staff/add', methods=['GET','POST'])
def add_staff():
    if request.method == 'GET':
        return render_template('staff/staff_add.html')
 
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        departmentID=request.form.get("departmentID")
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Insert_staff("+departmentID +",%s, %s, %s, %s);", (fname,lname,email,phone))
        mysqldb.commit()
        return redirect('/staff')

#Staff Update
@app.route('/staff/update', methods=['GET','POST'])
def update_staff():
    if request.method == 'GET':
        return render_template('staff/staff_update.html')
 
    if request.method == 'POST':
        staffID= request.form.get("staffID")
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        departmentID=request.form.get("departmentID")
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Update_staff("+staffID+","+departmentID+",%s, %s, %s, %s);", (fname,lname,email,phone))
        mysqldb.commit()
        return redirect('/staff')
#Staff Delete
@app.route('/staff/delete', methods=['GET','POST'])
def delete_staff():
    if request.method == 'GET':
        return render_template('staff/staff_delete.html')
 
    if request.method == 'POST':
        staffID = request.form.get('staffID')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Delete_Staff("+staffID+");")
        mysqldb.commit()
        return redirect('/staff')



#Manager Select
@app.route('/manager', methods=['GET','POST'])
def get_managers():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_manager;")
    res = []
    for row in cursor:
        res.append(row)
    return render_template('manager/manager.html',managers=res)

#Manager Insert
@app.route('/manager/add', methods=['GET','POST'])
def add_managers():
    if request.method == 'GET':
        return render_template('manager/manager_add.html')
 
    if request.method == 'POST':
        managerID = request.form.get('managerID')
        departmentID = request.form.get('departmentID')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Insert_Manager("+managerID+","+departmentID+");")
        mysqldb.commit()
        return redirect('/manager')

#Manager Update
@app.route('/manager/update', methods=['GET','POST'])
def update_managers():
    if request.method == 'GET':
        return render_template('manager/manager_update.html')
 
    if request.method == 'POST':
        managerID = request.form.get('managerID')
        departmentID = request.form.get('departmentID')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Update_Manager("+managerID+");")
        mysqldb.commit()
        return redirect('/manager')

#Manager Delete
@app.route('/manager/delete', methods=['GET','POST'])
def delete_managers():
    if request.method == 'GET':
        return render_template('manager/manager_delete.html')
 
    if request.method == 'POST':
        managerID = request.form.get('managerID')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Delete_Manager("+managerID+");")
        mysqldb.commit()
        return redirect('/manager')


#MedicalStaff Select
@app.route('/medicalstaff', methods=['GET','POST'])
def get_MedicalStaffs():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_MedicalStaff;")
    res = []
    for row in cursor:
        res.append(row)
    return render_template('medicalstaff/medicalstaff.html',medicalstaffs=res)

#MedicalStaff Insert
@app.route('/medicalstaff/add', methods=['GET','POST'])
def add_MedicalStaffs():
    if request.method == 'GET':
        return render_template('medicalstaff/medicalstaff_add.html')
 
    if request.method == 'POST':
        medstaffID = request.form.get('medstaffID')
        scheduleID = request.form.get('scheduleID')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Insert_MedicalStaff("+medstaffID+","+scheduleID+");")
        mysqldb.commit()
        return redirect('/medicalstaff')

#MedicalStaff Update
@app.route('/medicalstaff/update', methods=['GET','POST'])
def update_MedicalStaffs():
    if request.method == 'GET':
        return render_template('medicalstaff/medicalstaff_update.html')
 
    if request.method == 'POST':
        medstaffID = request.form.get('medstaffID')
        scheduleID = request.form.get('scheduleID')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Update_MedicalStaff("+medstaffID+","+scheduleID+");")
        mysqldb.commit()
        return redirect('/medicalstaff')

#MedicalStaff Delete
@app.route('/medicalstaff/delete', methods=['GET','POST'])
def delete_MedicalStaffs():
    if request.method == 'GET':
        return render_template('medicalstaff/medicalstaff_delete.html')
 
    if request.method == 'POST':
        medstaffID = request.form.get('medstaffID')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Delete_MedicalStaff("+medstaffID+");")
        mysqldb.commit()
        return redirect('/medicalstaff')



#secretary Select
@app.route('/secretary', methods=['GET','POST'])
def get_secretarys():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_secretary;")
    res = []
    for row in cursor:
        res.append(row)
    return render_template('secretary/secretary.html',secretaries=res)

#secretary Insert
@app.route('/secretary/add', methods=['GET','POST'])
def add_secretarys():
    if request.method == 'GET':
        return render_template('secretary/secretary_add.html')
 
    if request.method == 'POST':
        secretaryID = request.form.get('secretaryID')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Insert_secretary("+secretaryID+");")
        mysqldb.commit()
        return redirect('/secretary')


#No Update for secretary

#secretary Delete
@app.route('/secretary/delete', methods=['GET','POST'])
def delete_secretarys():
    if request.method == 'GET':
        return render_template('secretary/secretary_delete.html')
 
    if request.method == 'POST':
        secretaryID = request.form.get('secretaryID')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Delete_secretary("+secretaryID+");")
        mysqldb.commit()
        return redirect('/secretary')


#medicine Select
@app.route('/medicine', methods=['GET','POST'])
def get_medicines():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_medecine;")
    res = []
    for row in cursor:
        res.append(row)
    return render_template('medicine/medicine.html',medicines=res)

#medicine Insert
@app.route('/medicine/add', methods=['GET','POST'])
def add_medicines():
    if request.method == 'GET':
        return render_template('medicine/medicine_add.html')
 
    if request.method == 'POST':
        medname = request.form.get('medname')
        inventory = request.form.get('inventory')
        meddescription = request.form.get('meddescription')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Insert_Medicine("+medname+","+inventory+',test'+");")
        mysqldb.commit()
        return redirect('/medicine')


#medicine Update
@app.route('/medicine/update', methods=['GET','POST'])
def update_medicines():
    if request.method == 'GET':
        return render_template('medicine/medicine_update.html')
 
    if request.method == 'POST':
        medicineID=request.form.get('medicineID')
        medname = request.form.get('medname')
        inventory = request.form.get('inventory')
        meddescription = request.form.get('meddescription')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Update_Medicine("+medicineID+","+medname+","+inventory+", "+meddescription+");")
        mysqldb.commit()
        return redirect('/medicine')

#medicine Delete
@app.route('/medicine/delete', methods=['GET','POST'])
def delete_medicines():
    if request.method == 'GET':
        return render_template('medicine/medicine_delete.html')
 
    if request.method == 'POST':
        medicineID=request.form.get('medicineID')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Delete_medicine("+medicineID+");")
        mysqldb.commit()
        return redirect('/medicine')


#department Select
@app.route('/department', methods=['GET','POST'])
def get_departments():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_department;")
    res = []
    for row in cursor:
        res.append(row)
    return render_template('department.html',departments=res)

#department Insert
@app.route('/department/add', methods=['GET','POST'])
def add_departments():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Insert_department("+json["departmentName"]+");")
    mysqldb.commit()
    return 'success'

#department Update
@app.route('/department/update', methods=['GET','POST'])
def update_departments():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Update_department("+str(json["departmentID"])+","+json["departmentName"]+");")
    mysqldb.commit()
    return 'success'

#department Delete
@app.route('/department/delete', methods=['GET','POST'])
def delete_departments():
    cursor=mysqldb.cursor()
    json = request.json
    cursor.execute("call hospital.Delete_department("+str(json['departmentName'])+");")
    mysqldb.commit()
    return 'success'






#Appointement Add
@app.route('/appointments', methods=['POST'])
def get_appointments():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_appointment;")
    res = []
    for row in cursor:
        res.append(row)
    return jsonify(res)




 
