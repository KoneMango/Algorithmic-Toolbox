import cv2

# 打开摄像头
capture = cv2.VideoCapture(0)

# 获取摄像头的尺寸
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 循环读取每一帧图像
while True:
    # 读取一帧图像
    ret, frame = capture.read()

    # 将图像缩小为原来的一半
    frame = cv2.resize(frame, (width // 2, height // 2), interpolation=cv2.INTER_AREA)

    # 显示图像
    cv2.imshow('Camera', frame)

    # 等待按键，按下Q键退出循环
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# 关闭摄像头
capture.release()