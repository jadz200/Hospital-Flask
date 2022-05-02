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