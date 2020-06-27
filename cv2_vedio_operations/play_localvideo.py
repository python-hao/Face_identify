import cv2

#2、调用摄像头，创建窗口
vedio_path = r'D:\Documents\Bandicam\eurotrucks2 2020-06-16 11-18-18-153_Trim.mp4'
capture = cv2.VideoCapture(vedio_path)

while(capture.isOpened()):
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(30) == ord('q'):
        break