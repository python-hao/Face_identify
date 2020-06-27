"""


"""
import cv2

# cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap = cv2.VideoCapture(0)

# 人脸分类器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
face_cascade.load(r'D:\Python3.7\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml')
#获取数据
ret, frame = cap.read()
while(True):
    if not ret:
        cv2.waitKey(30)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # 人脸处理,画矩形图像 RGB (0-255)
    for (x, y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h),(255,0,0),1)



    cv2.imshow('v', frame)
    # 等待检测人脸 或 用户输入
    keyvalue = cv2.waitKey(30)
    # 点击键盘q 推出 &0xff表示键值
    if keyvalue & 0xff == ord('q'):
        break
# 窗口释放
cap.release()
cv2.destroyAllWindows()




