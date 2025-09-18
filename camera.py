# ls /dev/video*

# Agar error aaye libGL.so related, toh install karo:

# sudo apt-get install python3-opencv
# sudo apt-get install libgl1-mesa-glx

import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("USB Camera not detected")
    exit()

print("Press 'q' to quit, 's' to save snapshot")
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("USB Camera", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite("snapshot.jpg", frame)
        print("Snapshot saved as snapshot.jpg")

cap.release()
cv2.destroyAllWindows()


# see the image 
# xdg-open snapshot.jpg
