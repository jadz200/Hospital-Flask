create table Department (
	departmentID INT, 
    departmentName VARCHAR(200),
    Primary key(departmentID)
);
create table Manager (
	managerID INT, 
    departmentID INT,
    Primary key(managerID), 
    foreign key(departmentID) references Department(departmentID)
);

create table Staff(
	staffID INT, 
    departmentID INT, 
    fname VARCHAR(200), 
    lname VARCHAR(200), 
    email VARCHAR(30), 
    phoneNumber INT,
    primary Key(staffID), 
    foreign key(departmentID) references Department(departmentID)
);

create table Schedule(
	ScheduleID INT, 
    StartingTime DATETIME, 
    FinishTime DATETIME,
    primary key(ScheduleID)
);
create table MedicalStaff(
	MedStaffID INT, 
    scheduleID INT,
    primary key(MEdStaffID),
    foreign key(scheduleID) references Schedule(ScheduleID)
);
create table Doctor(
	DoctorID INT, specialization VARCHAR(200),
    primary key(DoctorID), 
    foreign key(DoctorID) references MedicalStaff(MedStaffID)
);

create table Nurse(
	NurseID INT,
    primary key(NurseID),
    foreign key(NurseID) references MedicalStaff(MedStaffID)
);
create table WorksWith(
	NurseID INT, 
    DoctorID INT,
    Primary Key(NurseID, DoctorID),
    foreign key(NurseID) references Nurse(NurseID),
    foreign key(DoctorID) references Doctor(DoctorID)
);
create table Medicine(
	MedicineID INT, 
    name VARCHAR(200), 
    inventory INT, 
    Description VARCHAR(200),
    primary key(MedicineID)
);
create table Secretary(
	SecretaryID INT, 
    primary Key(SecretaryID),
    foreign key(SecretaryID) references Staff(StaffID)
);
create table Room(
	RoomID INT, RoomNumber INT, Equipement VARCHAR(200),
    primary key(RoomID)
);
create Table Appointment(
	AppointmentID INT,
    SecretaryID INT, 
    ScheduleID INT, 
    RoomID INT, 
    StartingTime DATETIME, 
    FinishTime DATETIME,
    Primary Key(AppointmentID),
    foreign key(SecretaryID) references Secretary(SecretaryID),
    foreign Key(ScheduleID) references Schedule(ScheduleID),
    foreign key(RoomID) references Room(RoomID)
);
create table Patient(
	PatientID INT, 
    fname VARCHAR(200), 
    lname VARCHAR(200), 
    email VARCHAR(30), 
    phoneNumber VARCHAR(200),
    primary key(PatientID)
);
create table Insurance(
	InsuranceNumber INT,
    PatientID INT,
    class VARCHAR(100),
    company VARCHAR(200),
    Primary Key(InsuranceNumber),
    foreign key(PatientID) references Patient(PatientID)
);
create table PatientDependent(
	DependentID INT, 
    PatientID INT,
    fname VARCHAR(200), 
    lname VARCHAR(200), 
    relation VARCHAR(100),
    primary key(DependentID, PatientID),
    foreign key(PatientID) references Patient(PatientID)
);
create table Makes(
	MedicineID INT,
    DoctorID INT,
    AppoINTmentID INT,
    PatientID INT, 
    Bill INT,
    primary key(MedicineID, DoctorID, AppoINTmentID, PatientID),
    foreign key(MedicineID) references Medicine(MedicineID),
    foreign key(DoctorID) references Doctor(DoctorID),
    foreign key(AppoINTmentID) references AppoINTment(AppoINTmentID),
    foreign key(PatientID) references Patient(PatientID)
);