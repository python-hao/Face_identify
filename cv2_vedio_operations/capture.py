import cv2
from matplotlib import pyplot as plt

#1、调用摄像头，创建窗口
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# 获取捕获的分辨率,

# propTd 可以直接写数字，也可以用opencv的符号表示
# cap.get(propId)获取视频属性，cap.set(propId,value)设置视频属性
width, height = capture.get(3), capture.get(4)
print(width, height)

# 以原分辨率的已被来获取
capture.set(cv2.CAP_PROP_FRAME_WIDTH, width * 2)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height * 2)


while(True):
    # 获取一帧
    ret, frame = capture.read()
    # 将这帧转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

