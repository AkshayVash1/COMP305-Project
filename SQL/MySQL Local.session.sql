
CREATE TABLE Member (
    memberID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    ContactNumber VARCHAR(20),
    DateOfBirth DATE,
    FitnessGoals VARCHAR(255),
    LoyaltyPoints INT,
    trainerID INT,
    sessionID INT
);

CREATE TABLE Trainer (
    trainerID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    ContactNumber VARCHAR(20),
    DateOfBirth DATE,
    Certification VARCHAR(255),
    memberID INT,
    sessionID INT
);

CREATE TABLE Admin (
    adminID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    ContactNumber VARCHAR(20),
    DateOfBirth DATE,
    sessionID INT,
    resourceID INT
);

CREATE TABLE Session (
    sessionID INT PRIMARY KEY AUTO_INCREMENT,
    Date DATE,
    ProgressNotes TEXT,
    memberID INT,
    trainerID INT,
    adminID INT
);

CREATE TABLE ClubResources (
    resourceID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Status VARCHAR(50),
    adminID INT
);

ALTER TABLE Member
    ADD FOREIGN KEY (trainerID) REFERENCES Trainer(trainerID),
    ADD FOREIGN KEY (sessionID) REFERENCES Session(sessionID);

ALTER TABLE Trainer
    ADD FOREIGN KEY (memberID) REFERENCES Member(memberID),
    ADD FOREIGN KEY (sessionID) REFERENCES Session(sessionID);

ALTER TABLE Admin
    ADD FOREIGN KEY (sessionID) REFERENCES Session(sessionID),
    ADD FOREIGN KEY (resourceID) REFERENCES ClubResources(resourceID);

ALTER TABLE Session
    ADD FOREIGN KEY (memberID) REFERENCES Member(memberID),
    ADD FOREIGN KEY (trainerID) REFERENCES Trainer(trainerID),
    ADD FOREIGN KEY (adminID) REFERENCES Admin(adminID);

ALTER TABLE ClubResources
    ADD FOREIGN KEY (adminID) REFERENCES Admin(adminID);
