import serial
import time
import cv2

ser = serial.Serial('COM3', 9600, timeout=0)
bingo = cv2.imread('bingo.jpg', 0)
time.sleep(2)

ser.write(b'y')

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)

    ret = cv2.matchShapes(bingo, gray, 1, 0.0)
    print(ret)
    if(ret < 0.003):
        ser.write(b'y')
    # cv2.imwrite("bingo2.jpg", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()