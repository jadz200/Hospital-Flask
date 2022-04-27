CREATE schema Hospital;

CREATE TABLE Hospital.Department (
	departmentID INT NOT NULL, 
    departmentName VARCHAR(200) NOT NULL,
    PRIMARY KEY(departmentID)
);

CREATE TABLE Hospital.Manager (
	managerID INT NOT NULL, 
    departmentID INT NOT NULL,
    PRIMARY KEY(managerID), 
    FOREIGN KEY(departmentID) REFERENCES Hospital.Department(departmentID)
);

CREATE TABLE Hospital.Staff(
	staffID INT NOT NULL, 
    departmentID INT NOT NULL, 
    fname VARCHAR(200) NOT NULL, 
    lname VARCHAR(200) NOT NULL, 
    email VARCHAR(30) NOT NULL, 
    phoneNumber INT NOT NULL,
    PRIMARY KEY(staffID), 
    FOREIGN KEY(departmentID) REFERENCES Hospital.Department(departmentID)
);

CREATE TABLE Hospital.Schedule(
	ScheduleID INT NOT NULL, 
    StartingTime DATETIME NOT NULL, 
    FinishTime DATETIME NOT NULL,
    PRIMARY KEY(ScheduleID)
);

CREATE TABLE Hospital.MedicalStaff(
	MedStaffID INT NOT NULL, 
    scheduleID INT NOT NULL,
    PRIMARY KEY(MEdStaffID),
    FOREIGN KEY(scheduleID) REFERENCES Hospital.Schedule(ScheduleID)
);

CREATE TABLE Hospital.Doctor(
	DoctorID INT NOT NULL, 
    specialization VARCHAR(200) NOT NULL,
    PRIMARY KEY(DoctorID), 
    FOREIGN KEY(DoctorID) REFERENCES Hospital.MedicalStaff(MedStaffID)
);

CREATE TABLE Hospital.Nurse(
	NurseID INT NOT NULL,
    PRIMARY KEY(NurseID),
    FOREIGN KEY(NurseID) REFERENCES Hospital.MedicalStaff(MedStaffID)
);

CREATE TABLE Hospital.WorksWith(
	NurseID INT NOT NULL, 
    DoctorID INT NOT NULL,
    PRIMARY KEY(NurseID, DoctorID),
    FOREIGN KEY(NurseID) REFERENCES Hospital.Nurse(NurseID),
    FOREIGN KEY(DoctorID) REFERENCES Hospital.Doctor(DoctorID)
);

CREATE TABLE Hospital.Medicine(
	MedicineID INT NOT NULL, 
    name VARCHAR(200) NOT NULL, 
    inventory INT NOT NULL, 
    Description VARCHAR(200) NOT NULL,
    PRIMARY KEY(MedicineID)
);

CREATE TABLE Hospital.Secretary(
	SecretaryID INT NOT NULL, 
    PRIMARY KEY(SecretaryID),
    FOREIGN KEY(SecretaryID) REFERENCES Hospital.Staff(StaffID)
);

CREATE TABLE Hospital.Room(
	RoomID INT NOT NULL,
    RoomNumber INT NOT NULL,
    Equipement VARCHAR(200) NOT NULL,
    PRIMARY KEY(RoomID)
);

CREATE TABLE Hospital.Appointment(
	AppointmentID INT NOT NULL,
    SecretaryID INT NOT NULL, 
    ScheduleID INT NOT NULL, 
    RoomID INT NOT NULL, 
    StartingTime DATETIME NOT NULL, 
    FinishTime DATETIME NOT NULL,
    PRIMARY KEY(AppointmentID),
    FOREIGN KEY(SecretaryID) REFERENCES Hospital.Secretary(SecretaryID),
    FOREIGN KEY(ScheduleID) REFERENCES Hospital.Schedule(ScheduleID),
    FOREIGN KEY(RoomID) REFERENCES Hospital.Room(RoomID)
);

CREATE TABLE Hospital.Patient(
	CPatientID INT NOT NULL, 
    fname VARCHAR(200) NOT NULL, 
    lname VARCHAR(200) NOT NULL, 
    email VARCHAR(30) NOT NULL, 
    phoneNumber VARCHAR(200) NOT NULL,
    PRIMARY KEY(PatientID)
);

CREATE TABLE Hospital.Insurance(
	InsuranceNumber INT NOT NULL,
    PatientID INT NOT NULL,
    class VARCHAR(100) NOT NULL,
    company VARCHAR(200) NOT NULL,
    PRIMARY KEY(InsuranceNumber),
    FOREIGN KEY(PatientID) REFERENCES Hospital.Patient(PatientID)
);

CREATE TABLE Hospital.PatientDependent(
	DependentID INT NOT NULL, 
    PatientID INT NOT NULL,
    fname VARCHAR(200)  NOT NULL, 
    lname VARCHAR(200)  NOT NULL, 
    relation VARCHAR(100) NOT NULL,
    PRIMARY KEY(DependentID, PatientID),
    FOREIGN KEY(PatientID) REFERENCES Hospital.Patient(PatientID)
);

CREATE TABLE Hospital.Makes(
	MedicineID INT NOT NULL,
    DoctorID INT NOT NULL,
    AppointmentID INT NOT NULL,
    PatientID INT NOT NULL, 
    Bill INT NULL,
    PRIMARY KEY(MedicineID, DoctorID, AppointmentID, PatientID),
    FOREIGN KEY(MedicineID) REFERENCES Hospital.Medicine(MedicineID),
    FOREIGN KEY(DoctorID) REFERENCES Hospital.Doctor(DoctorID),
    FOREIGN KEY(AppointmentID) REFERENCES Hospital.Appointment(AppointmentID),
    FOREIGN KEY(PatientID) REFERENCES Hospital.Patient(PatientID)
);