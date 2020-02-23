import cv2
import numpy as np
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap=cv2.VideoCapture(0)
ret, frame1=cap.read()
ret,frame2=cap.read()

while(cap.isOpened()):
    # it calculate the diffrence between two farme
    diff=cv2.absdiff(frame1, frame2)
    # after calculating the frame changing to gray
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    # after We use GaussianBlur(change_value,color size,sigma x value)
    blur=cv2.GaussianBlur(gray, (5,5), 0)
    _, thersh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    # to better countor
    dilated=cv2.dilate(thersh, None, iterations=3)
    countors, _ =cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for coutour in countors:
        (x,y,w,h)=cv2.boundingRect(coutour)
        if cv2.contourArea(coutour)<700:
         continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame1, "Status: {}".format("Motion Detection"),(10,20),cv2.FONT_HERSHEY_SIMPLEX,
        1, (0,0,255),3)

    #cv2.drawContours(frame1,countors, -1, (0,255,0),2)
    if ret==True:
        # displaying the resulting image
        cv2.imshow("Frame",frame1)
        frame1=frame2
        ret,frame2=cap.read()
        # Press ESC on keyboard to  exit
        if cv2.waitKey(25)==27:
            break
# When everything done, release the video capture object
cv2.release()
# Closes all the frames
cv2.destroyAllWindows()
