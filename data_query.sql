INSERT INTO Team (name) VALUES ('Team A'), ('Team B');

-- Insert data into Stadium
INSERT INTO Stadium (name, location) VALUES ('Stadium 1', 'Location 1');

-- Insert data into Match
INSERT INTO `Match` (team1_id, team2_id, date, stadium_id) 
VALUES (1, 2, '2024-06-20', 1);

-- Insert data into User
INSERT INTO User (username, password, email) 
VALUES ('user1', 'password1', 'user1@example.com');

-- Insert data into Ticket
INSERT INTO Ticket (match_id, user_id, seat_number, price) 
VALUES (1, 1, 'A1', 50.00);

-- Insert data into Ticket_Type
INSERT INTO Ticket_Type (name, price) 
VALUES ('VIP', 100.00), ('Regular', 50.00);

-- Insert data into Payment
INSERT INTO Payment (user_id, ticket_id, amount, payment_date) 
VALUES (1, 1, 50.00, '2024-06-15');

-- Insert data into Seat
INSERT INTO Seat (stadium_id, seat_number, availability) 
VALUES (1, 'A1', TRUE);

-- Insert data into Match_Result
INSERT INTO Match_Result (match_id, team1_score, team2_score) 
VALUES (1, 3, 2);

-- Insert data into Referee
INSERT INTO Referee (name) 
VALUES ('Referee 1');

-- Insert data into Booking
INSERT INTO Booking (user_id, match_id, booking_date, status) 
VALUES (1, 1, '2024-06-15', 'confirmed');
-- Select all matches with team names and stadium details
SELECT m.match_id, t1.name AS team1, t2.name AS team2, m.date, s.name AS stadium, s.location
FROM `Match` m
JOIN Team t1 ON m.team1_id = t1.team_id
JOIN Team t2 ON m.team2_id = t2.team_id
JOIN Stadium s ON m.stadium_id = s.stadium_id;

-- Select all tickets with user and match details
SELECT t.ticket_id, u.username, m.date AS match_date, t.seat_number, t.price
FROM Ticket t
JOIN User u ON t.user_id = u.user_id
JOIN `Match` m ON t.match_id = m.match_id;

-- Select all payments with user and ticket details
SELECT p.payment_id, u.username, t.seat_number, p.amount, p.payment_date
FROM Payment p
JOIN User u ON p.user_id = u.user_id
JOIN Ticket t ON p.ticket_id = t.ticket_id;
-- Update the seat availability after booking a ticket
UPDATE Seat
SET availability = FALSE
WHERE stadium_id = 1 AND seat_number = 'A1';

-- Update the status of a booking
UPDATE Booking
SET status = 'confirmed'
WHERE booking_id = 1;
-- Delete a user and cascade the delete to related tickets and payments
DELETE FROM User WHERE user_id = 1;

-- Delete a match result
DELETE FROM Match_Result WHERE result_id = 1;
-- Select match details along with the scores, referee, and booking status for a user
SELECT m.match_id, t1.name AS team1, t2.name AS team2, m.date, s.name AS stadium, s.location, 
       r.name AS referee, mr.team1_score, mr.team2_score, b.status
FROM `Match` m
JOIN Team t1 ON m.team1_id = t1.team_id
JOIN Team t2 ON m.team2_id = t2.team_id
JOIN Stadium s ON m.stadium_id = s.stadium_id
JOIN Match_Result mr ON m.match_id = mr.match_id
JOIN Booking b ON m.match_id = b.match_id
JOIN User u ON b.user_id = u.user_id
JOIN Referee r ON m.match_id = r.referee_id
WHERE u.user_id = 1;
