import serial

def rfid_read():
    ser = None
    try:
        ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)
        print("Reading ...")
        while True:
            data = ser.read(12)
            if data:
                tag = data.decode('utf-8').strip()
                print(f"RFID tag: {tag}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if ser:
            ser.close()

if __name__ == "__main__":
    rfid_read()



#
import serial

def rfid_read():
    ser = None
    try:
        card = ['1E005BAAB45B']  # valid RFID card list
        ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)
        print("Reading ...")
        while True:
            data = ser.read(12)
            if data:
                tag = data.decode('utf-8').strip()
                if tag in card:
                    print("Valid entry")
                else:
                    print("Invalid entry")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if ser:
            ser.close()

if __name__ == "__main__":
    rfid_read()


# # Print valid and Invalid RFID tags
import serial

def rfid_read():
    ser = None
    try:
        # List of valid RFID card IDs
        valid_cards = ['1E005BAAB45B', '2A008CDFA123', '3B009XYZA789']
        
        ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)
        print("Reading RFID tags...")

        while True:
            data = ser.read(12)  # read 12 bytes from RFID
            if data:
                tag = data.decode('utf-8').strip()
                if tag in valid_cards:
                    print(f"Valid tag: {tag}")
                else:
                    print(f"Invalid tag: {tag}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if ser:
            ser.close()

if __name__ == "__main__":
    rfid_read()



# Menu driven python code for - Register new card, Mark Attendance, Delete card.
import serial
import os
import datetime

CARDS_FILE = "cards.txt"
ATTENDANCE_FILE = "attendance.txt"

# ----------- Helper Functions -----------

def load_cards():
    if not os.path.exists(CARDS_FILE):
        return []
    with open(CARDS_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_cards(cards):
    with open(CARDS_FILE, "w") as f:
        for card in cards:
            f.write(card + "\n")

def log_attendance(card):
    with open(ATTENDANCE_FILE, "a") as f:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{card} - Present at {now}\n")

# ----------- RFID Reader -----------

def read_rfid():
    try:
        ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)
        print("Scan RFID card...")
        data = ser.read(12)
        ser.close()
        if data:
            return data.decode('utf-8').strip()
    except Exception as e:
        print(f"Error: {e}")
    return None

# ----------- Menu Operations -----------

def register_card():
    cards = load_cards()
    tag = read_rfid()
    if tag:
        if tag not in cards:
            cards.append(tag)
            save_cards(cards)
            print(f"Card {tag} registered successfully!")
        else:
            print("Card already registered.")
    else:
        print("No card detected.")

def mark_attendance():
    cards = load_cards()
    tag = read_rfid()
    if tag:
        if tag in cards:
            print(f"Valid card {tag}. Attendance marked.")
            log_attendance(tag)
        else:
            print(f"Invalid card {tag}.")
    else:
        print("No card detected.")

def delete_card():
    cards = load_cards()
    tag = read_rfid()
    if tag:
        if tag in cards:
            cards.remove(tag)
            save_cards(cards)
            print(f"Card {tag} deleted successfully.")
        else:
            print("Card not found.")
    else:
        print("No card detected.")

# ----------- Main Menu -----------

def menu():
    while True:
        print("\n=== RFID Attendance System ===")
        print("1. Register New Card")
        print("2. Mark Attendance")
        print("3. Delete Card")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register_card()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            delete_card()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

# ----------- Run -----------

if __name__ == "__main__":
    menu()



## Saving Data in mysql database 

# databse 
# CREATE DATABASE rfid_system;

# USE rfid_system;

# CREATE TABLE cards (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     tag VARCHAR(50) UNIQUE NOT NULL
# );

# CREATE TABLE attendance (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     tag VARCHAR(50) NOT NULL,
#     timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
# );

  # # Python code to interact with MySQL database
import serial
import mysql.connector
import datetime

# -------- MySQL Connection --------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",      # change if needed
        user="root",           # your MySQL username
        password="password",   # your MySQL password
        database="rfid_system"
    )

# -------- RFID Reader --------
def read_rfid():
    try:
        ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)
        print("Scan RFID card...")
        data = ser.read(12)
        ser.close()
        if data:
            return data.decode('utf-8').strip()
    except Exception as e:
        print(f"Error: {e}")
    return None

# -------- Menu Functions --------
def register_card():
    tag = read_rfid()
    if tag:
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO cards (tag) VALUES (%s)", (tag,))
            conn.commit()
            print(f"Card {tag} registered successfully!")
        except mysql.connector.IntegrityError:
            print("Card already registered.")
        finally:
            cursor.close()
            conn.close()
    else:
        print("No card detected.")

def mark_attendance():
    tag = read_rfid()
    if tag:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cards WHERE tag=%s", (tag,))
        card = cursor.fetchone()
        if card:
            cursor.execute("INSERT INTO attendance (tag) VALUES (%s)", (tag,))
            conn.commit()
            print(f"Valid card {tag}. Attendance marked.")
        else:
            print(f"Invalid card {tag}.")
        cursor.close()
        conn.close()
    else:
        print("No card detected.")

def delete_card():
    tag = read_rfid()
    if tag:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cards WHERE tag=%s", (tag,))
        if cursor.rowcount > 0:
            conn.commit()
            print(f"Card {tag} deleted successfully.")
        else:
            print("Card not found.")
        cursor.close()
        conn.close()
    else:
        print("No card detected.")

# -------- Main Menu --------
def menu():
    while True:
        print("\n=== RFID Attendance System (MySQL) ===")
        print("1. Register New Card")
        print("2. Mark Attendance")
        print("3. Delete Card")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register_card()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            delete_card()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

# -------- Run --------
if __name__ == "__main__":
    menu()

