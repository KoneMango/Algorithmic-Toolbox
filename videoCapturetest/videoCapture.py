import cv2
import os
os.chdir('C:\\Users\\will\Documents\\GitHub\\Algorithmic_Toolbox\\videoCapturetest')

# 加载人脸检测器,级联分类器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#DNN 人脸检测器
#face_cascade = cv2.dnn.readNetFromCaffe('deploy.prototxt.txt', 'res10_300x300_ssd_iter_140000.caffemodel')

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取摄像头中的一帧图像
    _, img = cap.read()

    # 将图像转换为灰度图像
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 检测图像中的人脸
    faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)

    #使用DNN检测人脸
    # blob = cv2.dnn.blobFromImage(img, 1.0, (300, 300), (104.0, 177.0, 123.0))
    # face_cascade.setInput(blob)
    # faces = face_cascade.forward()


    # 在图像中标记人脸
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # 显示识别结果
    cv2.imshow('Video', img)

    # 按 q 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 关闭摄像头
cap.release()