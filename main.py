import datetime
import decimal

import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': '11111111',
    'host': '127.0.0.1',
    'database': 'Soccer_management_system'
}

# Function to connect to the MySQL database
def connect_to_database():
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        print("Connected to the database successfully.")
        return cnx, cursor
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None, None

def insert_user(cursor, cnx):
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")
        email = input("Enter email: ")
        add_user = ("INSERT INTO User (username, password, email) "
                    "VALUES (%s, %s, %s)")
        data_user = (username, password, email)
        cursor.execute(add_user, data_user)
        cnx.commit()
        print("User added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def insert_team(cursor, cnx):
    try:
        uzbek_teams = [
            'Pakhtakor', 'Navbahor Namangan', 'Nasaf Qarshi',
            'Bunyodkor', 'Lokomotiv Tashkent', 'Metallurg Bekabad',
            'Sogdiana Jizzakh', 'Surkhon Termez', 'Mashal Mubarek',
            'Andijan', 'Kokand 1912', 'Qizilqum Zarafshon'
        ]
        for team in uzbek_teams:
            add_team = ("INSERT INTO Team (name) VALUES (%s)")
            data_team = (team,)
            cursor.execute(add_team, data_team)
        cnx.commit()
        print("Uzbek teams added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def insert_stadium(cursor, cnx):
    try:
        stadiums = [
            ("Bunyodkor Stadium", "Tashkent"),
            ("Nasaf Stadium", "Karshi"),
            ("Babur Arena", "Andijan"),
            ("Pakhtakor Centeral Stadium", "Tashkent")
        ]
        for name, location in stadiums:
            add_stadium = ("INSERT INTO Stadium (name, location) VALUES (%s, %s)")
            data_stadium = (name, location)
            cursor.execute(add_stadium, data_stadium)
        cnx.commit()
        print("Stadiums added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def insert_match(cursor, cnx):
    try:
        cursor.execute("SELECT team_id, name FROM Team")
        teams = cursor.fetchall()
        print("Teams:")
        for team in teams:
            print(f"{team[0]}: {team[1]}")

        team1_id = int(input("Enter team 1 ID: "))
        team2_id = int(input("Enter team 2 ID: "))
        date = input("Enter match date (YYYY-MM-DD): ")

        cursor.execute("SELECT stadium_id, name FROM Stadium")
        stadiums = cursor.fetchall()
        print("Stadiums:")
        for stadium in stadiums:
            print(f"{stadium[0]}: {stadium[1]}")

        stadium_id = int(input("Enter stadium ID: "))

        add_match = ("INSERT INTO `Match` (team1_id, team2_id, date, stadium_id) "
                     "VALUES (%s, %s, %s, %s)")
        data_match = (team1_id, team2_id, date, stadium_id)
        cursor.execute(add_match, data_match)
        cnx.commit()
        print("Match added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def insert_ticket(cursor, cnx):
    try:
        cursor.execute("SELECT match_id, team1_id, team2_id, date FROM `Match`")
        matches = cursor.fetchall()
        print("Matches:")
        for match in matches:
            print(f"{match[0]}: {match[1]} vs {match[2]} on {match[3]}")

        match_id = int(input("Enter match ID: "))

        cursor.execute("SELECT user_id, username FROM User")
        users = cursor.fetchall()
        print("Users:")
        for user in users:
            print(f"{user[0]}: {user[1]}")

        user_id = int(input("Enter user ID: "))

        seat_number = input("Enter seat number: ")
        price = float(input("Enter ticket price: "))

        add_ticket = ("INSERT INTO Ticket (match_id, user_id, seat_number, price) "
                      "VALUES (%s, %s, %s, %s)")
        data_ticket = (match_id, user_id, seat_number, price)
        cursor.execute(add_ticket, data_ticket)
        cnx.commit()
        print("Ticket added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def insert_ticket_type(cursor, cnx):
    try:
        name = input("Enter ticket type name: ")
        price = float(input("Enter ticket type price: "))
        add_ticket_type = ("INSERT INTO Ticket_Type (name, price) VALUES (%s, %s)")
        data_ticket_type = (name, price)
        cursor.execute(add_ticket_type, data_ticket_type)
        cnx.commit()
        print("Ticket type added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def insert_payment(cursor, cnx):
    try:
        cursor.execute("SELECT user_id, username FROM User")
        users = cursor.fetchall()
        print("Users:")
        for user in users:
            print(f"{user[0]}: {user[1]}")

        user_id = int(input("Enter user ID: "))

        cursor.execute("SELECT ticket_id, match_id, seat_number FROM Ticket")
        tickets = cursor.fetchall()
        print("Tickets:")
        for ticket in tickets:
            print(f"{ticket[0]}: Match {ticket[1]}, Seat {ticket[2]}")

        ticket_id = int(input("Enter ticket ID: "))

        amount = float(input("Enter payment amount: "))
        payment_date = input("Enter payment date (YYYY-MM-DD): ")

        add_payment = ("INSERT INTO Payment (user_id, ticket_id, amount, payment_date) "
                       "VALUES (%s, %s, %s, %s)")
        data_payment = (user_id, ticket_id, amount, payment_date)
        cursor.execute(add_payment, data_payment)
        cnx.commit()
        print("Payment added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def insert_seat(cursor, cnx):
    try:
        cursor.execute("SELECT stadium_id, name FROM Stadium")
        stadiums = cursor.fetchall()
        print("Stadiums:")
        for stadium in stadiums:
            print(f"{stadium[0]}: {stadium[1]}")

        stadium_id = int(input("Enter stadium ID: "))
        seat_number = input("Enter seat number: ")
        availability = bool(int(input("Enter seat availability (1 for True, 0 for False): ")))

        add_seat = ("INSERT INTO Seat (stadium_id, seat_number, availability) "
                    "VALUES (%s, %s, %s)")
        data_seat = (stadium_id, seat_number, availability)
        cursor.execute(add_seat, data_seat)
        cnx.commit()
        print("Seat added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to insert data into Match_Result table
def insert_match_result(cursor, cnx):
    try:
        cursor.execute("SELECT match_id, team1_id, team2_id, date FROM `Match`")
        matches = cursor.fetchall()
        print("Matches:")
        for match in matches:
            print(f"{match[0]}: {match[1]} vs {match[2]} on {match[3]}")

        match_id = int(input("Enter match ID: "))
        team1_score = int(input("Enter team 1 score: "))
        team2_score = int(input("Enter team 2 score: "))

        add_match_result = ("INSERT INTO Match_Result (match_id, team1_score, team2_score) "
                            "VALUES (%s, %s, %s)")
        data_match_result = (match_id, team1_score, team2_score)
        cursor.execute(add_match_result, data_match_result)
        cnx.commit()
        print("Match result added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to insert data into Referee table
def insert_referee(cursor, cnx):
    try:
        name = input("Enter referee name: ")
        add_referee = ("INSERT INTO Referee (name) VALUES (%s)")
        data_referee = (name,)
        cursor.execute(add_referee, data_referee)
        cnx.commit()
        print("Referee added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def insert_booking(cursor, cnx):
    try:
        cursor.execute("SELECT user_id, username FROM User")
        users = cursor.fetchall()
        print("Users:")
        for user in users:
            print(f"{user[0]}: {user[1]}")

        user_id = int(input("Enter user ID: "))

        cursor.execute("SELECT match_id, team1_id, team2_id, date FROM `Match`")
        matches = cursor.fetchall()
        print("Matches:")
        for match in matches:
            print(f"{match[0]}: {match[1]} vs {match[2]} on {match[3]}")

        match_id = int(input("Enter match ID: "))
        booking_date = input("Enter booking date (YYYY-MM-DD): ")
        status = input("Enter booking status (pending or confirmed): ")

        add_booking = ("INSERT INTO Booking (user_id, match_id, booking_date, status) "
                       "VALUES (%s, %s, %s, %s)")
        data_booking = (user_id, match_id, booking_date, status)
        cursor.execute(add_booking, data_booking)
        cnx.commit()
        print("Booking added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def display_table_data(cursor, table_name):
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        print(f"\nData from {table_name.replace('`', '')} table:")
        for row in rows:
            print(row)
    except mysql.connector.Error as err:
        print(f"Error fetching data from {table_name.replace('`', '')} table: {err}")

def main():
    cnx, cursor = connect_to_database()
    if cnx is None or cursor is None:
        return

    try:
        while True:
            choice = menu()
            if choice == 0:
                break
            elif choice in range(1, 12):
                function_map = {
                    1: insert_user,
                    2: insert_team,
                    3: insert_stadium,
                    4: insert_match,
                    5: insert_ticket,
                    6: insert_ticket_type,
                    7: insert_payment,
                    8: insert_seat,
                    9: insert_match_result,
                    10: insert_referee,
                    11: insert_booking
                }
                function_map[choice](cursor, cnx)
            else:
                print("Invalid choice. Please try again.")

        # Display data from all tables at the end
        table_names = ['User', 'Team', 'Stadium', '`Match`', 'Ticket', 'Ticket_Type',
                       'Payment', 'Seat', 'Match_Result', 'Referee', 'Booking']
        for table_name in table_names:
            display_table_data(cursor, table_name)

    finally:
        cursor.close()
        cnx.close()


# Menu to select which data to insert
def menu():
    print("\nMenu:")
    print("1. Insert User")
    print("2. Insert Team (Uzbekistan teams)")
    print("3. Insert Stadium")
    print("4. Insert Match")
    print("5. Insert Ticket")
    print("6. Insert Ticket Type")
    print("7. Insert Payment")
    print("8. Insert Seat")
    print("9. Insert Match Result")
    print("10. Insert Referee")
    print("11. Insert Booking")
    print("0. Exit")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 0 <= choice <= 11:
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 11.")

# Main program
# Function to display data from tables
def display_table_data(cursor, table_name):
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        print(f"\nData from {table_name.replace('`', '')} table:")

        for row in rows:
            formatted_row = []
            for item in row:
                if isinstance(item, decimal.Decimal):
                    formatted_row.append(f"{item:.2f}")  # Format decimal to two decimal places
                elif isinstance(item, datetime.date):
                    formatted_row.append(item.strftime("%Y-%m-%d"))  # Format date as YYYY-MM-DD
                else:
                    formatted_row.append(item)
            print(tuple(formatted_row))
    except mysql.connector.Error as err:
        print(f"Error fetching data from {table_name.replace('`', '')} table: {err}")

# Main program
def main():
    cnx, cursor = connect_to_database()
    if cnx is None or cursor is None:
        return

    try:
        while True:
            choice = menu()
            if choice == 0:
                break
            elif choice in range(1, 12):
                function_map = {
                    1: insert_user,
                    2: insert_team,
                    3: insert_stadium,
                    4: insert_match,
                    5: insert_ticket,
                    6: insert_ticket_type,
                    7: insert_payment,
                    8: insert_seat,
                    9: insert_match_result,
                    10: insert_referee,
                    11: insert_booking
                }
                function_map[choice](cursor, cnx)
            else:
                print("Invalid choice. Please try again.")

        # Display data from all tables at the end
        table_names = ['User', 'Team', 'Stadium', '`Match`', 'Ticket', 'Ticket_Type',
                       'Payment', 'Seat', 'Match_Result', 'Referee', 'Booking']
        for table_name in table_names:
            display_table_data(cursor, table_name)

    finally:
        cursor.close()
        cnx.close()

if __name__ == "__main__":
    main()
