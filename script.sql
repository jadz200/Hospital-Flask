CREATE schema Hospital;

CREATE TABLE Hospital.Department (
	departmentID INT NOT NULL auto_increment, 
    departmentName VARCHAR(200) NOT NULL,
    PRIMARY KEY(departmentID)
);

CREATE TABLE Hospital.Manager (
	managerID INT(5) ZEROFILL NOT NULL PRIMARY KEY , 
    departmentID INT NOT NULL,
	FOREIGN KEY(managerID) REFERENCES Hospital.Department(staffID),
    FOREIGN KEY(departmentID) REFERENCES Hospital.Department(departmentID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE = MYISAM;

CREATE TABLE Hospital.Staff(
	staffID INT(5)  ZEROFILL NOT NULL AUTO_INCREMENT ,
    departmentID INT NOT NULL, 
    fname VARCHAR(200) NOT NULL, 
    lname VARCHAR(200) NOT NULL, 
    email VARCHAR(30) NOT NULL, 
    phoneNumber VARCHAR(30) NOT NULL,
    PRIMARY KEY(staffID), 
    FOREIGN KEY(departmentID) REFERENCES Hospital.Department(departmentID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Hospital.Schedule(
	ScheduleID INT NOT NULL AUTO_INCREMENT, 
    StartingTime DATETIME NOT NULL, 
    FinishTime DATETIME NOT NULL,
    PRIMARY KEY(ScheduleID)
);

CREATE TABLE Hospital.MedicalStaff(
	MedStaffID INT(5) ZEROFILL NOT NULL, 
    scheduleID INT NOT NULL,
    PRIMARY KEY(MEdStaffID),
    FOREIGN KEY(scheduleID) REFERENCES Hospital.Schedule(ScheduleID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Hospital.Doctor(
	DoctorID INT(5) ZEROFILL NOT NULL, 
    specialization VARCHAR(200) NOT NULL,
    PRIMARY KEY(DoctorID), 
    FOREIGN KEY(DoctorID) REFERENCES Hospital.MedicalStaff(MedStaffID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Hospital.Nurse(
	NurseID INT(5) ZEROFILL NOT NULL,
    PRIMARY KEY(NurseID),
    FOREIGN KEY(NurseID) REFERENCES Hospital.MedicalStaff(MedStaffID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Hospital.WorksWith(
	NurseID INT(5) ZEROFILL NOT NULL, 
    DoctorID INT(5) ZEROFILL NOT NULL,
    PRIMARY KEY(NurseID, DoctorID),
    FOREIGN KEY(NurseID) REFERENCES Hospital.Nurse(NurseID),
    FOREIGN KEY(DoctorID) REFERENCES Hospital.Doctor(DoctorID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Hospital.Medicine(
	MedicineID INT(3) ZEROFILL NOT NULL AUTO_INCREMENT, 
    name VARCHAR(200) NOT NULL, 
    inventory INT NOT NULL, 
    Description VARCHAR(2000) NOT NULL,
    PRIMARY KEY(MedicineID)
);

CREATE TABLE Hospital.Secretary(
	SecretaryID INT(5) ZEROFILL NOT NULL, 
    PRIMARY KEY(SecretaryID),
    FOREIGN KEY(SecretaryID) REFERENCES Hospital.Staff(StaffID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Hospital.Room(
	RoomID INT NOT NULL AUTO_INCREMENT,
    RoomNumber CHAR(3) NOT NULL,
    Equipement VARCHAR(200) NOT NULL,
    PRIMARY KEY(RoomID)
);

CREATE TABLE Hospital.Appointment(
	AppointmentID INT NOT NULL AUTO_INCREMENT,
    SecretaryID INT(5) ZEROFILL NOT NULL, 
    ScheduleID INT NOT NULL, 
    RoomID INT NOT NULL, 
    StartingTime DATETIME NOT NULL, 
    FinishTime DATETIME NOT NULL,
    PRIMARY KEY(AppointmentID),
    FOREIGN KEY(SecretaryID) REFERENCES Hospital.Secretary(SecretaryID),
    FOREIGN KEY(ScheduleID) REFERENCES Hospital.Schedule(ScheduleID),
    FOREIGN KEY(RoomID) REFERENCES Hospital.Room(RoomID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Hospital.Patient(
	PatientID INT(5) ZEROFILL NOT NULL AUTO_INCREMENT, 
    fname VARCHAR(200) NOT NULL, 
    lname VARCHAR(200) NOT NULL, 
    email VARCHAR(200) NOT NULL, 
    phoneNumber VARCHAR(200) NOT NULL,
    PRIMARY KEY(PatientID)
);

CREATE TABLE Hospital.Insurance(
	InsuranceNumber CHAR(10) NOT NULL ,
    PatientID INT(5) ZEROFILL NOT NULL,
    class ENUM("Bronze", "Silver", "Gold","Platinum") NOT NULL,
    company VARCHAR(200) NOT NULL,
    PRIMARY KEY(InsuranceNumber),
    FOREIGN KEY(PatientID) REFERENCES Hospital.Patient(PatientID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Hospital.PatientDependent(
	DependentID INT(5) ZEROFILL NOT NULL AUTO_INCREMENT, 
    PatientID INT(5) ZEROFILL NOT NULL,
    fname VARCHAR(200)  NOT NULL, 
    lname VARCHAR(200)  NOT NULL, 
    relation ENUM('Brother','Sister','Mother','Father','Grandmother','Grandfather','Uncle','Aunt','Cousin','Wife') NOT NULL,
    PRIMARY KEY(DependentID, PatientID),
    FOREIGN KEY(PatientID) REFERENCES Hospital.Patient(PatientID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Hospital.Makes(
	MedicineID INT(3) ZEROFILL NOT NULL auto_increment,
    DoctorID INT(5) ZEROFILL NOT NULL,
    AppointmentID INT NOT NULL,
    PatientID INT(5) ZEROFILL NOT NULL, 
    Bill INT NULL,
    PRIMARY KEY(MedicineID, DoctorID, AppointmentID, PatientID),
    FOREIGN KEY(MedicineID) REFERENCES Hospital.Medicine(MedicineID),
    FOREIGN KEY(DoctorID) REFERENCES Hospital.Doctor(DoctorID),
    FOREIGN KEY(AppointmentID) REFERENCES Hospital.Appointment(AppointmentID),
    FOREIGN KEY(PatientID) REFERENCES Hospital.Patient(PatientID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


INSERT INTO hospital.DEPARTMENT(departmentName) VALUES("Cardiology");
INSERT INTO hospital.DEPARTMENT(departmentName) VALUES("Radiology");
INSERT INTO hospital.DEPARTMENT(departmentName) VALUES("Paramedical");
INSERT INTO hospital.DEPARTMENT(departmentName) VALUES("Dietary");
INSERT INTO hospital.DEPARTMENT(departmentName) VALUES("Rehabilitation");

INSERT INTO hospital.Staff(departmentID,fname,lname,email,phoneNumber) VALUES(1,"Jad","Zarzour","jadzarzour3@gmail.com","+96171849906");
INSERT INTO hospital.Staff(departmentID,fname,lname,email,phoneNumber) VALUES(2,"Emillie","Watts","emilliewatts@gmail.com","+96170857869");
INSERT INTO hospital.Staff(departmentID,fname,lname,email,phoneNumber) VALUES(3,"Jason","Tomlison","jasontomlison@gmail.com","+96176457274");
INSERT INTO hospital.Staff(departmentID,fname,lname,email,phoneNumber) VALUES(5,"Damian","Price","damianprice@gmail.com","+96176737568");
INSERT INTO hospital.Staff(departmentID,fname,lname,email,phoneNumber) VALUES(2,"Nathan","Bentley","nathanbentley@gmail.com","+96176161475");
INSERT INTO hospital.Staff(departmentID,fname,lname,email,phoneNumber) VALUES(3,"Marcel","Rigby","marcelrigby@gmail.com","+96176045024");
INSERT INTO hospital.Staff(departmentID,fname,lname,email,phoneNumber) VALUES(4,"Claudia","Guerra","claudiaguerra@gmail.com","+96176457");
INSERT INTO hospital.Staff(departmentID,fname,lname,email,phoneNumber) VALUES(1,"Kimberley","Baldwin","kimberleybaldwin@gmail.com","+96176172907");
INSERT INTO hospital.Staff(departmentID,fname,lname,email,phoneNumber) VALUES(3,"Justin","Callahan","justincallahan@gmail.com","+96176158801");
INSERT INTO hospital.Staff(departmentID,fname,lname,email,phoneNumber) VALUES(1,"Rhianna","Middleton","rihanamiddleton@gmail.com","+96176930714");
INSERT INTO hospital.Staff(departmentID,fname,lname,email,phoneNumber) VALUES(4,"Nathaniel","Michael","nathanielmicheal@gmail.com","+96176076755");
INSERT INTO hospital.Staff(departmentID,fname,lname,email,phoneNumber) VALUES(5,"Sheila","Potter","sheilapotter@gmail.com","+96176555834");
INSERT INTO hospital.Staff(departmentID,fname,lname,email,phoneNumber) VALUES(3,"Hussain","Marks","hussainmarks@gmail.com","+9617655508");
INSERT INTO hospital.Staff(departmentID,fname,lname,email,phoneNumber) VALUES(4,"Dwayne","Dawson","lucillemariott@gmail.com","+96135559466");
INSERT INTO hospital.Staff(departmentID,fname,lname,email,phoneNumber) VALUES(1,"Douglas","Howe","douglashowe@gmail.com","+9617055522");
INSERT INTO hospital.Staff(departmentID,fname,lname,email,phoneNumber) VALUES(5,"Alissia","Romero","alissiaromero@gmail.com","+9613555029");
INSERT INTO hospital.Staff(departmentID,fname,lname,email,phoneNumber) VALUES(2,"Daniel","Church","danielchurch@gmail.com","+96176555459");
INSERT INTO hospital.Staff(departmentID,fname,lname,email,phoneNumber) VALUES(4,"Axel","Hope","axelhope@gmail.com","+96176563459");


INSERT INTO hospital.manager VALUES(00001,1);
INSERT INTO hospital.manager VALUES(00002,2);
INSERT INTO hospital.manager VALUES(00003,3);
INSERT INTO hospital.manager VALUES(00004,5);
INSERT INTO hospital.manager VALUES(00007,4);

INSERT INTO hospital.Secretary(SecretaryID) VALUES(00018);
INSERT INTO hospital.Secretary(SecretaryID) VALUES(00013);
INSERT INTO hospital.Secretary(SecretaryID) VALUES(00014);
INSERT INTO hospital.Secretary(SecretaryID) VALUES(00015);
INSERT INTO hospital.Secretary(SecretaryID) VALUES(00016);
INSERT INTO hospital.Secretary(SecretaryID) VALUES(00017);

INSERT INTO hospital.schedule(StartingTime,FinishTime) VALUES("2022-05-03 07:00:00","2015-05-03 17:00:00");
INSERT INTO hospital.schedule(StartingTime,FinishTime) VALUES("2022-05-03 09:00:00","2015-05-03 15:00:00");
INSERT INTO hospital.schedule(StartingTime,FinishTime) VALUES("2022-05-03 05:45:00","2015-05-03 12:00:00");
INSERT INTO hospital.schedule(StartingTime,FinishTime) VALUES("2022-05-03 06:15:00","2015-05-03 13:00:00");
INSERT INTO hospital.schedule(StartingTime,FinishTime) VALUES("2022-05-03 08:30:00","2015-05-03 15:00:00");
INSERT INTO hospital.schedule(StartingTime,FinishTime) VALUES("2022-06-03 07:00:00","2015-06-03 14:40:00");
INSERT INTO hospital.schedule(StartingTime,FinishTime) VALUES("2022-07-03 10:00:00","2015-07-03 18:00:00");

INSERT INTO hospital.Appointment(SecretaryID,ScheduleID,RoomID,StartingTime,FinishTime) VALUES(00018,1,1,"2022-05-03 07:00:00","2015-05-03 07:30:00");
INSERT INTO hospital.Appointment(SecretaryID,ScheduleID,RoomID,StartingTime,FinishTime) VALUES(00013,1,2,"2022-05-03 08:00:00","2015-05-03 09:00:00");
INSERT INTO hospital.Appointment(SecretaryID,ScheduleID,RoomID,StartingTime,FinishTime) VALUES(00012,1,5,"2022-05-03 10:00:00","2015-05-03 11:30:00");
INSERT INTO hospital.Appointment(SecretaryID,ScheduleID,RoomID,StartingTime,FinishTime) VALUES(00013,2,1,"2022-05-03 09:00:00","2015-05-03 10:30:00");
INSERT INTO hospital.Appointment(SecretaryID,ScheduleID,RoomID,StartingTime,FinishTime) VALUES(00014,2,5,"2022-05-03 12:00:00","2015-05-03 13:00:00");
INSERT INTO hospital.Appointment(SecretaryID,ScheduleID,RoomID,StartingTime,FinishTime) VALUES(00016,2,1,"2022-05-03 13:00:00","2015-05-03 14:00:00");
INSERT INTO hospital.Appointment(SecretaryID,ScheduleID,RoomID,StartingTime,FinishTime) VALUES(00014,3,3,"2022-05-03 06:00:00","2015-05-03 07:30:00");
INSERT INTO hospital.Appointment(SecretaryID,ScheduleID,RoomID,StartingTime,FinishTime) VALUES(00015,3,4,"2022-05-03 07:00:00","2015-05-03 07:30:00");
INSERT INTO hospital.Appointment(SecretaryID,ScheduleID,RoomID,StartingTime,FinishTime) VALUES(00018,5,2,"2022-05-03 07:00:00","2015-05-03 07:30:00");
INSERT INTO hospital.Appointment(SecretaryID,ScheduleID,RoomID,StartingTime,FinishTime) VALUES(00012,6,1,"2022-05-03 07:00:00","2015-05-03 07:30:00");
INSERT INTO hospital.Appointment(SecretaryID,ScheduleID,RoomID,StartingTime,FinishTime) VALUES(00018,3,2,"2022-05-03 07:00:00","2015-05-03 07:30:00");
INSERT INTO hospital.Appointment(SecretaryID,ScheduleID,RoomID,StartingTime,FinishTime) VALUES(00016,4,3,"2022-05-03 07:00:00","2015-05-03 07:30:00");
INSERT INTO hospital.Appointment(SecretaryID,ScheduleID,RoomID,StartingTime,FinishTime) VALUES(00014,4,6,"2022-05-03 07:00:00","2015-05-03 07:30:00");
INSERT INTO hospital.Appointment(SecretaryID,ScheduleID,RoomID,StartingTime,FinishTime) VALUES(00015,6,3,"2022-05-03 07:00:00","2015-05-03 07:30:00");
INSERT INTO hospital.Appointment(SecretaryID,ScheduleID,RoomID,StartingTime,FinishTime) VALUES(00016,7,7,"2022-05-03 07:00:00","2015-05-03 07:30:00");

INSERT INTO hospital.MedicalStaff(MedStaffID, scheduleID) VALUES(00005,1);
INSERT INTO hospital.MedicalStaff(MedStaffID, scheduleID) VALUES(00006,2);
INSERT INTO hospital.MedicalStaff(MedStaffID, scheduleID) VALUES(00008,3);
INSERT INTO hospital.MedicalStaff(MedStaffID, scheduleID) VALUES(00009,4);
INSERT INTO hospital.MedicalStaff(MedStaffID, scheduleID) VALUES(00010,5);
INSERT INTO hospital.MedicalStaff(MedStaffID, scheduleID) VALUES(00011,6);
INSERT INTO hospital.MedicalStaff(MedStaffID, scheduleID) VALUES(00012,7);

INSERT INTO hospital.Doctor(DoctorID,specialization) VALUES (00005,"Radiologist");
INSERT INTO hospital.Doctor(DoctorID,specialization) VALUES (00006,"Paramedic");
INSERT INTO hospital.Doctor(DoctorID,specialization) VALUES (00008,"Cardiologist");
INSERT INTO hospital.Doctor(DoctorID,specialization) VALUES (00009,"Paramedic");

INSERT INTO hospital.Nurse(NurseID) VALUES(00010);
INSERT INTO hospital.Nurse(NurseID) VALUES(00011);
INSERT INTO hospital.Nurse(NurseID) VALUES(00012);

INSERT INTO hospital.WorksWith(NurseID,DoctorID) VALUES(00010,00005); 
INSERT INTO hospital.WorksWith(NurseID,DoctorID) VALUES(00010,00006); 
INSERT INTO hospital.WorksWith(NurseID,DoctorID) VALUES(00011,00005); 
INSERT INTO hospital.WorksWith(NurseID,DoctorID) VALUES(00011,00009); 
INSERT INTO hospital.WorksWith(NurseID,DoctorID) VALUES(00012,00008); 




INSERT INTO hospital.room (RoomNumber,Equipement)VALUES("101","");
INSERT INTO hospital.room (RoomNumber,Equipement)VALUES("121","");
INSERT INTO hospital.room (RoomNumber,Equipement)VALUES("141","");
INSERT INTO hospital.room (RoomNumber,Equipement)VALUES("151","");
INSERT INTO hospital.room (RoomNumber,Equipement)VALUES("153","");
INSERT INTO hospital.room (RoomNumber,Equipement)VALUES("189","");
INSERT INTO hospital.room (RoomNumber,Equipement)VALUES("203","");
INSERT INTO hospital.room (RoomNumber,Equipement)VALUES("305","");



INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Rome","Field","romefield@gmail.com","+9617155538");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Kaif","lland","kaiflland@gmail.com","+9617155554");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Rohaan", "Mackay","rohaanmackay@gmail.com","+9617655593");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Tahir", "Mays","tahirmays@gmail.com","+9617055586");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Remi", "Dunn","remidunn@gmail.com","+9617055544");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Kaleb","Todd","kalebtodd@gmail.com","+9617655549");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Emilio", "Oliver","emiliooliver@gmail.com","+9617655554");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Rhona","quivel","rhonaquivel@gmail.com","+9613555894");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Jessica","onaldson","jessicaonaldson@gmail.com","+9617155532");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Evelyn","Schmitt","evelynschmitt@gmail.com","+9617055573");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Isla","ooley","islaooley@gmail.com","+9613555490");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Fynley","Patrick","fynleypatrick@gmail.com","+9617655513");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES('Alesha',"Hoffman","aleshahoffman@gmail.com","+9617655511");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Ioana","arrish","ioanaarrish@gmail.com","+9617155508");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Braxton","Wilde","braxtononwilde@gmail.com","+9617155500");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Iolo","Cross","iolocross@gmail.com","+9617655557");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Sharna","illiams","sharnailliams@gmail.com","+9617655571");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES('Floyd',"ambert","floydambert@gmail.com","+9617055545");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Hanan","ritton","hananritton@gmail.com","+9617155588");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Lawson","ingston","lawsoningston@gmail.com","+9613555296");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Tilly","Enriquez","tillyenriquez@gmail.com","+9617055547");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Jarrad","Gates","jarradgates@gmail.com","+9613555513");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Nazifa","Kearney","nazifakearney@gmail.com","+9617155564");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Nicola", "Chaney","nicolachaney@gmail.com","+9617155539");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Mariella","Paul","mariellapaul@gmail.com","+9617155525");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Bridie","itworth","bridieitworth@gmail.com","+9617655589");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Azeem","Dolan","azeemdolan@gmail.com","+9617655570");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Todd","teman","toddteman@gmail.com","+9617155546");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Tiana","lacruz","tianalacruz@gmail.com","+9617155560");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Neriah","Maxwell","neriahmaxwell@gmail.com","+9613555918");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Emmanuel","Roy","emmanuelroy@gmail.com","+9617155574");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Lynn","nnell","lynnnnell@gmail.com","+9617055575");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Luciano","Feeney","lucianofeeney@gmail.com","+9613555674");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Jackson","Doe","jacksondoe@gmail.com","+9617655575");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Dennis","Kane","denniskane@gmail.com","+9617655542");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Ezekiel","Cornish","ezekielcornish@gmail.com","+9617055546");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Riley","James","rileyjames@gmail.com","+9617155527");
INSERT INTO hospital.Patient(fname,lname,email,phoneNumber) VALUES("Lachlan","Sandoval","lachlansandoval@gmail.com","+9617655514");

INSERT INTO hospital.Insurance(InsuranceNumber,PatientID,class,company) VALUES("1230581391",00001,"Bronze","NextCare");
INSERT INTO hospital.Insurance(InsuranceNumber,PatientID,class,company) VALUES("5431973037",00002,"Silver","Medicare");
INSERT INTO hospital.Insurance(InsuranceNumber,PatientID,class,company) VALUES("4861595580",00003,"Platinum","Medicaid");
INSERT INTO hospital.Insurance(InsuranceNumber,PatientID,class,company) VALUES("4510062139",00004,"Gold","NextCare");
INSERT INTO hospital.Insurance(InsuranceNumber,PatientID,class,company) VALUES("2992803309",00005,"Bronze","Medicare");
INSERT INTO hospital.Insurance(InsuranceNumber,PatientID,class,company) VALUES("5617417738",00006,"Silver","NextCare");
INSERT INTO hospital.Insurance(InsuranceNumber,PatientID,class,company) VALUES("8122052489",00007,"Gold","Medicaid");
INSERT INTO hospital.Insurance(InsuranceNumber,PatientID,class,company) VALUES("9746304855",00008,"Platinum","Medicare");
INSERT INTO hospital.Insurance(InsuranceNumber,PatientID,class,company) VALUES("9706897627",00009,"Silver","Medicare");
INSERT INTO hospital.Insurance(InsuranceNumber,PatientID,class,company) VALUES("3913210008",00010,"Gold","NextCare");
INSERT INTO hospital.Insurance(InsuranceNumber,PatientID,class,company) VALUES("4622587027",00011,"Silver","Medicaid");
INSERT INTO hospital.Insurance(InsuranceNumber,PatientID,class,company) VALUES("8147263220",00012,"Bronze","NextCare");
INSERT INTO hospital.Insurance(InsuranceNumber,PatientID,class,company) VALUES("0202684121",00001,"Platinum","Medicaid");
INSERT INTO hospital.Insurance(InsuranceNumber,PatientID,class,company) VALUES("2536209138",00013,"Bronze","NextCare");



INSERT INTO hospital.Medicine(name,inventory,Description) VALUES("Actos",50,"Actos (pioglitazone) is an oral diabetes medicine that helps control blood sugar levels.");
INSERT INTO hospital.Medicine(name,inventory,Description) VALUES("Botox",14,"Botox is used in adults to treat cervical dystonia (abnormal head position and neck pain).");
INSERT INTO hospital.Medicine(name,inventory,Description) VALUES("Fentanyl",20,"Fentanyl patches are used when other pain treatments such as non-opioid pain medicines or immediate-release opioid medicines do not treat your pain well enough or you cannot tolerate them.");
INSERT INTO hospital.Medicine(name,inventory,Description) VALUES("Ferrous Sulfate",50,"Ferrous sulfate is used to treat iron deficiency anemia (a lack of red blood cells caused by having too little iron in the body).");
INSERT INTO hospital.Medicine(name,inventory,Description) VALUES("Fish Oil",100,"Fish Oil are used together with diet and exercise to help lower triglyceride levels in the blood.");
INSERT INTO hospital.Medicine(name,inventory,Description) VALUES("Shingrix Vaccine",50,"Shingrix is used to prevent herpes zoster virus (shingles)");
INSERT INTO hospital.Medicine(name,inventory,Description) VALUES("Sutent",50,"Sutent is a prescription medicine used to treat certain types of advanced or progressive tumors of the stomach, intestines, esophagus, pancreas, or kidneys.");


INSERT INTO hospital.PatientDependent(PatientID,fname,lname,relation) VALUES(00001,"Sam","Kane","Cousin");
INSERT INTO hospital.PatientDependent(PatientID,fname,lname,relation) VALUES(00001,"Lena","Jefferson","Sister");
INSERT INTO hospital.PatientDependent(PatientID,fname,lname,relation) VALUES(00002,"Sallie","Floyd","Mother");
INSERT INTO hospital.PatientDependent(PatientID,fname,lname,relation) VALUES(00003,"Meadow","Heath","Aunt");
INSERT INTO hospital.PatientDependent(PatientID,fname,lname,relation) VALUES(00004,"Tatiana","Cross","Cousin");
INSERT INTO hospital.PatientDependent(PatientID,fname,lname,relation) VALUES(00001,"Addison","Ramos","Cousin");
INSERT INTO hospital.PatientDependent(PatientID,fname,lname,relation) VALUES(00005,"Priya","Needham","Cousin");
INSERT INTO hospital.PatientDependent(PatientID,fname,lname,relation) VALUES(00003,"Anna","Stephenson","Cousin");
INSERT INTO hospital.PatientDependent(PatientID,fname,lname,relation) VALUES(00008,"Henna","Clements","Brother");
INSERT INTO hospital.PatientDependent(PatientID,fname,lname,relation) VALUES(00009,"Dominick","Griffith","Brother");
INSERT INTO hospital.PatientDependent(PatientID,fname,lname,relation) VALUES(00010,"Daria","Rollins","Brother");
INSERT INTO hospital.PatientDependent(PatientID,fname,lname,relation) VALUES(00011,"Daniaal","Mccall","Brother");
INSERT INTO hospital.PatientDependent(PatientID,fname,lname,relation) VALUES(00013,"Kain","Gibson","Brother");
INSERT INTO hospital.PatientDependent(PatientID,fname,lname,relation) VALUES(00015,"Steffan","Pierce","Father");
INSERT INTO hospital.PatientDependent(PatientID,fname,lname,relation) VALUES(00004,"Reyansh","Wilkins","Brother");
INSERT INTO hospital.PatientDependent(PatientID,fname,lname,relation) VALUES(00003,"Shaunna","Stevenson","Brother");
INSERT INTO hospital.PatientDependent(PatientID,fname,lname,relation) VALUES(00003,"Maxime","Searle","Father");
INSERT INTO hospital.PatientDependent(PatientID,fname,lname,relation) VALUES(00002,"Rojin","Chang","Uncle");
INSERT INTO hospital.PatientDependent(PatientID,fname,lname,relation) VALUES(00011,"Emmett","Ray","Brother");
INSERT INTO hospital.PatientDependent(PatientID,fname,lname,relation) VALUES(00017,"Simeon","Livingston","Cousin");
