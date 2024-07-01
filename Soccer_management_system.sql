CREATE DATABASE IF NOT EXISTS Soccer_management_system;

USE Soccer_management_system;

-- Disable foreign key checks to drop tables safely
SET FOREIGN_KEY_CHECKS=0;

-- Drop existing tables
DROP TABLE IF EXISTS Booking;
DROP TABLE IF EXISTS Payment;
DROP TABLE IF EXISTS Ticket;
DROP TABLE IF EXISTS Match_Result;
DROP TABLE IF EXISTS Seat;
DROP TABLE IF EXISTS Referee;
DROP TABLE IF EXISTS `Match`;
DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Stadium;
DROP TABLE IF EXISTS Ticket_Type;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS bericht;

-- Re-enable foreign key checks
SET FOREIGN_KEY_CHECKS=1;

-- Create User table
CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

-- Create Team table
CREATE TABLE Team (
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Create Stadium table
CREATE TABLE Stadium (
    stadium_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL
);

-- Create Match table
CREATE TABLE `Match` (
    match_id INT AUTO_INCREMENT PRIMARY KEY,
    team1_id INT,
    team2_id INT,
    date DATE,
    stadium_id INT,
    FOREIGN KEY (team1_id) REFERENCES Team(team_id),
    FOREIGN KEY (team2_id) REFERENCES Team(team_id),
    FOREIGN KEY (stadium_id) REFERENCES Stadium(stadium_id)
);

-- Create Ticket table
CREATE TABLE Ticket (
    ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    match_id INT,
    user_id INT,
    seat_number VARCHAR(50),
    price DECIMAL(10, 2),
    FOREIGN KEY (match_id) REFERENCES `Match`(match_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- Create Ticket_Type table
CREATE TABLE Ticket_Type (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Create Payment table
CREATE TABLE Payment (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    ticket_id INT,
    amount DECIMAL(10, 2),
    payment_date DATE,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (ticket_id) REFERENCES Ticket(ticket_id)
);

-- Create Seat table
CREATE TABLE Seat (
    seat_id INT AUTO_INCREMENT PRIMARY KEY,
    stadium_id INT,
    seat_number VARCHAR(50),
    availability BOOLEAN,
    FOREIGN KEY (stadium_id) REFERENCES Stadium(stadium_id)
);

-- Create Match_Result table
CREATE TABLE Match_Result (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    match_id INT,
    team1_score INT,
    team2_score INT,
    FOREIGN KEY (match_id) REFERENCES `Match`(match_id)
);

-- Create Referee table
CREATE TABLE Referee (
    referee_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Create Booking table
CREATE TABLE Booking (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    match_id INT,
    booking_date DATE,
    status ENUM('pending', 'confirmed') DEFAULT 'pending',
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (match_id) REFERENCES `Match`(match_id)
);
show tables;