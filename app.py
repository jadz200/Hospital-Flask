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
        cursor.execute("call hospital.Insert_Medicine(\""+medname+"\",\'"+inventory+"\',\'"+meddescription+"\');")
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
        cursor.execute("call hospital.Update_Medicine(\'"+medicineID+"\',\'"+medname+"\',\'"+inventory+"\', \'"+meddescription+"\');")
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
        cursor.execute("call hospital.Delete_medicine(\'"+medicineID+"\');")
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
    return render_template('department/department.html',departments=res)

#department Insert
@app.route('/department/add', methods=['GET','POST'])
def add_departments():
    if request.method == 'GET':
        return render_template('department/department_add.html')
 
    if request.method == 'POST':
        departmentName=request.form.get('departmentName')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Insert_department(\'"+departmentName+"\');")
        mysqldb.commit()
        return redirect('/department')

#department Update
@app.route('/department/update', methods=['GET','POST'])
def update_departments():
    if request.method == 'GET':
        return render_template('department/department_update.html')
 
    if request.method == 'POST':
        departmentID=request.form.get('departmentID')
        departmentName=request.form.get('departmentName')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Update_department(\'"+departmentID+"\',\'"+departmentName+"\');")
        mysqldb.commit()
        return redirect('/department')

#department Delete
@app.route('/department/delete', methods=['GET','POST'])
def delete_departments():
    if request.method == 'GET':
        return render_template('department/department_delete.html')
 
    if request.method == 'POST':
        departmentName=request.form.get('departmentName')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Delete_department(\'"+departmentName+"\');")
        mysqldb.commit()
        return redirect('/department')

#schedule Select
@app.route('/schedule', methods=['GET','POST'])
def get_schedules():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_schedule;")
    res = []
    for row in cursor:
        res.append(row)
    return render_template('schedule/schedule.html',schedules=res)

#schedule Insert
@app.route('/schedule/add', methods=['GET','POST'])
def add_schedules():
    if request.method == 'GET':
        return render_template('schedule/schedule_add.html')
 
    if request.method == 'POST':
        StartingTime=request.form.get('StartingTime')
        FinishTime=request.form.get('FinishTime')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Insert_schedule(\'"+StartingTime+"\',\'"+FinishTime+"\');")
        mysqldb.commit()
        return redirect('/schedule')

#schedule Update
@app.route('/schedule/update', methods=['GET','POST'])
def update_schedules():
    if request.method == 'GET':
        return render_template('schedule/schedule_update.html')
 
    if request.method == 'POST':
        scheduleID=request.form.get('scheduleID')
        StartingTime=request.form.get('StartingTime')
        FinishTime=request.form.get('FinishTime')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Update_schedule(\'"+scheduleID+"\',\'"+StartingTime+"\',\'"+FinishTime+"\');")
        mysqldb.commit()
        return redirect('/schedule')

#schedule Delete
@app.route('/schedule/delete', methods=['GET','POST'])
def delete_schedules():
    if request.method == 'GET':
        return render_template('schedule/schedule_delete.html')
 
    if request.method == 'POST':
        scheduleID=request.form.get('scheduleID')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Delete_schedule(\'"+scheduleID+"\');")
        mysqldb.commit()
        return redirect('/schedule')






#Appointement View
@app.route('/appointment', methods=['GET','POST'])
def get_appointments():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_appointment;")
    res = []
    for row in cursor:
        res.append(row)
    return render_template('appointment/appointment.html',appointments=res)

#Appointement Inserts

@app.route('/appointment/add', methods=['GET','POST'])
def add_appointments():
    if request.method == 'GET':
        return render_template('appointment/appointment_add.html')
 
    if request.method == 'POST':
        secretaryID=request.form.get('secretaryID')
        scheduleID=request.form.get('scheduleID')
        roomID=request.form.get('roomID')
        StartingTime=request.form.get('StartingTime')
        FinishTime=request.form.get('FinishTime')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Insert_appointment(\'"+secretaryID+"\',\'"+scheduleID+"\',\'"+roomID+"\',\'"+StartingTime+"\',\'"+FinishTime+"\');")
        mysqldb.commit()
        return redirect('/appointment')

#appointment Update
@app.route('/appointment/update', methods=['GET','POST'])
def update_appointments():
    if request.method == 'GET':
        return render_template('appointment/appointment_update.html')
 
    if request.method == 'POST':
        appointmentID=request.form.get('appointmentID')
        secretaryID=request.form.get('secretaryID')
        scheduleID=request.form.get('scheduleID')
        roomID=request.form.get('roomID')
        StartingTime=request.form.get('StartingTime')
        FinishTime=request.form.get('FinishTime')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Update_appointment(\'"+appointmentID+"\',\'"+secretaryID+"\',\'"+scheduleID+"\',\'"+roomID+"\',\'"+StartingTime+"\',\'"+FinishTime+"\');")
        mysqldb.commit()
        return redirect('/appointment')

#appointment Delete
@app.route('/appointment/delete', methods=['GET','POST'])
def delete_appointments():
    if request.method == 'GET':
        return render_template('appointment/appointment_delete.html')
 
    if request.method == 'POST':
        appointmentID=request.form.get('appointmentID')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Delete_appointment(\'"+appointmentID+"\');")
        mysqldb.commit()
        return redirect('/appointment')



#room Select
@app.route('/room', methods=['GET','POST'])
def get_rooms():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_room;")
    res = []
    for row in cursor:
        res.append(row)
    return render_template('room/room.html',rooms=res)

#room Insert
@app.route('/room/add', methods=['GET','POST'])
def add_rooms():
    if request.method == 'GET':
        return render_template('room/room_add.html')
 
    if request.method == 'POST':
        roomNumber=request.form.get('roomNumber')
        equipement=request.form.get('equipement')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Insert_Room(\'"+str(roomNumber)+"\',\'"+equipement+"\');")
        mysqldb.commit()
        return redirect('/room')

#room Update
@app.route('/room/update', methods=['GET','POST'])
def update_rooms():
    if request.method == 'GET':
        return render_template('room/room_update.html')
 
    if request.method == 'POST':
        roomID=request.form.get('roomID')
        roomNumber=request.form.get('roomNumber')
        equipement=request.form.get('equipement')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Update_room(\'"+roomID+"\',\'"+roomNumber+"\',\'"+equipement+"\');")
        mysqldb.commit()
        return redirect('/room')

#room Delete
@app.route('/room/delete', methods=['GET','POST'])
def delete_rooms():
    if request.method == 'GET':
        return render_template('room/room_delete.html')
 
    if request.method == 'POST':
        roomID=request.form.get('roomID')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Delete_room(\'"+roomID+"\');")
        mysqldb.commit()
        return redirect('/room')

 
#patientDependent Select
@app.route('/patientDependent', methods=['GET','POST'])
def get_patientDependents():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_patient_dependent;")
    res = []
    for row in cursor:
        res.append(row)
    return render_template('patientDependent/patientDependent.html',patientDependents=res)

#patientDependent Insert
@app.route('/patientDependent/add', methods=['GET','POST'])
def add_patientDependents():
    if request.method == 'GET':
        return render_template('patientDependent/patientDependent_add.html')
 
    if request.method == 'POST':
        patientID=request.form.get('patientID')
        fname=request.form.get('fname')
        lname=request.form.get('lname')
        relation=request.form.get('relation')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Insert_patientDependent(\'"+patientID+"\',\'"+fname+"\',\'"+lname+"\',\'"+relation+"\');")
        mysqldb.commit()
        return redirect('/patientDependent')

#patientDependent Update
@app.route('/patientDependent/update', methods=['GET','POST'])
def update_patientDependents():
    if request.method == 'GET':
        return render_template('patientDependent/patientDependent_update.html')
 
    if request.method == 'POST':
        patientDependentID=request.form.get('patientDependentID')
        patientID=request.form.get('patientID')
        fname=request.form.get('fname')
        lname=request.form.get('lname')
        relation=request.form.get('relation')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Update_PatientDependent(\'"+patientDependentID+"\',\'"+patientID+"\',\'"+fname+"\',\'"+lname+"\',\'"+relation+"\');")
        mysqldb.commit()
        return redirect('/patientDependent')

#patientDependent Delete
@app.route('/patientDependent/delete', methods=['GET','POST'])
def delete_patientDependents():
    if request.method == 'GET':
        return render_template('patientDependent/patientDependent_delete.html')
 
    if request.method == 'POST':
        patientDependentID=request.form.get('patientDependentID')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Delete_patientDependent(\'"+patientDependentID+"\');")
        mysqldb.commit()
        return redirect('/patientDependent')
    
    #insurance Select
@app.route('/insurance', methods=['GET','POST'])
def get_insurances():
    cursor=mysqldb.cursor()
    cursor.execute("SELECT * FROM hospital.get_insurance;")
    res = []
    for row in cursor:
        res.append(row)
    return render_template('insurance/insurance.html',insurances=res)

#insurance Insert
@app.route('/insurance/add', methods=['GET','POST'])
def add_insurances():
    if request.method == 'GET':
        return render_template('insurance/insurance_add.html')
 
    if request.method == 'POST':
        insuranceNumber=request.form.get('insuranceNumber')
        patientID=request.form.get('patientID')
        insclass=request.form.get('class')
        company=request.form.get('company')

        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Insert_insurance(\'"+str(insuranceNumber)+"\',\'"+patientID+"\',\'"+insclass+"\',\'"+company+"\');")
        mysqldb.commit()
        return redirect('/insurance')

#insurance Update
@app.route('/insurance/update', methods=['GET','POST'])
def update_insurances():
    if request.method == 'GET':
        return render_template('insurance/insurance_update.html')
 
    if request.method == 'POST':
        insuranceNumber=request.form.get('insuranceNumber')
        patientID=request.form.get('patientID')
        insclass=request.form.get('class')
        company=request.form.get('company')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Update_insurance(\'"+str(insuranceNumber)+"\',\'"+patientID+"\',\'"+insclass+"\',\'"+company+"\');")
        mysqldb.commit()
        return redirect('/insurance')

#insurance Delete
@app.route('/insurance/delete', methods=['GET','POST'])
def delete_insurances():
    if request.method == 'GET':
        return render_template('insurance/insurance_delete.html')
 
    if request.method == 'POST':
        insuranceNumber=request.form.get('insuranceNumber')
        cursor=mysqldb.cursor()
        cursor.execute("call hospital.Delete_insurance(\'"+insuranceNumber+"\');")
        mysqldb.commit()
        return redirect('/insurance')