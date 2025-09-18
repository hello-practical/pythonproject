# Corrected Code (Enroll Finger)
import time
from pyfingerprint.pyfingerprint import PyFingerprint

try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if f.verifyPassword() == False:
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('Fingerprint sensor initialization failed!')
    print('Exception message: ' + str(e))
    exit(1)


def enrollFinger():
    try:
        print('Waiting for finger...')

        # Wait until a finger is read
        while f.readImage() == False:
            pass

        # Convert first read image
        f.convertImage(0x01)

        print('Remove finger...')
        time.sleep(2)

        print('Waiting for same finger again...')

        # Wait for second read
        while f.readImage() == False:
            pass

        # Convert second read image
        f.convertImage(0x02)

        # Compare characteristics
        if f.compareCharacteristics() == 0:
            print("Fingers do not match")
            return

        # Create template
        f.createTemplate()

        # Store template in sensor
        positionNumber = f.storeTemplate()
        print('Finger enrolled successfully!')
        print('New template position #' + str(positionNumber))

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)


if __name__ == '__main__':
    enrollFinger()
    # searchFinger()
    # deleteFinger()


# # Complete Code: Fingerprint Menu System
import time
from pyfingerprint.pyfingerprint import PyFingerprint


# --------- Connect Fingerprint Sensor ---------
try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if f.verifyPassword() == False:
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('Fingerprint sensor initialization failed!')
    print('Exception message: ' + str(e))
    exit(1)


# --------- Enroll Finger ---------
def enrollFinger():
    try:
        print('Waiting for finger...')

        while f.readImage() == False:
            pass

        f.convertImage(0x01)

        print('Remove finger...')
        time.sleep(2)

        print('Waiting for same finger again...')

        while f.readImage() == False:
            pass

        f.convertImage(0x02)

        if f.compareCharacteristics() == 0:
            print("Fingers do not match")
            return

        f.createTemplate()
        positionNumber = f.storeTemplate()
        print('Finger enrolled successfully!')
        print('New template position #' + str(positionNumber))

    except Exception as e:
        print('Enrollment failed!')
        print('Exception message: ' + str(e))


# --------- Search Finger ---------
def searchFinger():
    try:
        print('Waiting for finger...')

        while f.readImage() == False:
            pass

        f.convertImage(0x01)

        result = f.searchTemplate()

        positionNumber = result[0]

        if positionNumber == -1:
            print("No match found!")
            return

        print(f"Finger found at position #{positionNumber}")
        print("Attendance Marked ✅")

    except Exception as e:
        print('Search failed!')
        print('Exception message: ' + str(e))


# --------- Delete Finger ---------
def deleteFinger():
    try:
        positionNumber = int(input("Enter template position number to delete: "))
        if f.deleteTemplate(positionNumber) == True:
            print("Template deleted successfully!")
    except Exception as e:
        print('Delete failed!')
        print('Exception message: ' + str(e))


# --------- Menu ---------
def menu():
    while True:
        print("\n=== Fingerprint Attendance System ===")
        print("1. Enroll New Finger")
        print("2. Verify Finger (Mark Attendance)")
        print("3. Delete Finger")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            enrollFinger()
        elif choice == "2":
            searchFinger()
        elif choice == "3":
            deleteFinger()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
