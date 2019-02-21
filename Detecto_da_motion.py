import  cv2, time
##testing video capture using cv2


firts_frame=None
video = cv2.VideoCapture(1)


while True:


    check,frame = video.read()


    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)

    if firts_frame is None:
        firts_frame=gray
        continue

    delta_frame = cv2.absdiff(firts_frame,gray)
    thresh_fram=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_fram=cv2.dilate(thresh_fram,None,iterations=2)

    (_,cnts,_)=cv2.findContours(thresh_fram.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000 :
            continue
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+y,y+h),(0,255,0),3)

    cv2.imshow("Gray",gray)
    cv2.imshow("delta",delta_frame)
    cv2.imshow("thresh",thresh_fram)

    key=cv2.waitKey(1)
    print(frame)
    print(delta_frame)
    if key ==ord('q'):
        break
        video.release()
        cv2.destroyAllWindows()