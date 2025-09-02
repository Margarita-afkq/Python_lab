import time
import cv2
import numpy as np

def image_processing():
    img = cv2.imread('images/variant-3.jpeg')
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV Image', img_hsv)
    cv2.waitKey(0)

def video_processing():
    cap = cv2.VideoCapture(1)
    down_points = (640, 480)
    i = 0

    center_region = (down_points[0]//2 - 100, down_points[1]//2 - 100, 200, 200)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        cv2.rectangle(frame, 
                     (center_region[0], center_region[1]),
                     (center_region[0] + center_region[2], center_region[1] + center_region[3]),
                     (255, 0, 0), 2)
        
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
           
            marker_center_x = x + w//2
            marker_center_y = y + h//2
            
            if (center_region[0] <= marker_center_x <= center_region[0] + center_region[2] and
                center_region[1] <= marker_center_y <= center_region[1] + center_region[3]):
                cv2.putText(frame, 'IN CENTER', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                           1, (0, 255, 0), 2, cv2.LINE_AA)
            else:
                cv2.putText(frame, 'NOT IN CENTER', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                           1, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)
        i += 1

    cap.release()

if __name__ == '__main__':
    image_processing()
    video_processing()

cv2.destroyAllWindows()
