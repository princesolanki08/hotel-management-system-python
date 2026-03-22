create database hotel_management;
USE hotel_management;
CREATE TABLE customer (
    Name VARCHAR(100),
    Gender VARCHAR(10),
    Mobile VARCHAR(15) PRIMARY KEY,
    Email VARCHAR(100),
    Nationality VARCHAR(50),
    Idproof VARCHAR(50),
    Idnumber VARCHAR(50)
);

CREATE TABLE room (
    contact VARCHAR(15) NOT NULL,
    checkin DATE NOT NULL,
    checkout DATE NOT NULL,
    roomtype VARCHAR(50),
    roomavailable VARCHAR(10),
    meal VARCHAR(50),
    noofdays INT,
    paidtax DECIMAL(10,2),
    subtotal DECIMAL(10,2),
    total DECIMAL(10,2),
    PRIMARY KEY (contact)
);