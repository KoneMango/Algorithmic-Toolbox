import numpy as nps
import cv2
#从文件中读取一张图片
def read_image(path):
    img = cv2.imread(path)
    return img  
#主函数，弹出框让用户选择一张图片
if __name__=="__main__":
    print('Please select an image')
    path = "C:/Users/will/Desktop/gront.jpg"
    img = read_image(path)
    resized_image = cv2.resize(img, (600, 400))
    cv2.imshow('image',resized_image)
    cv2.resizeWindow('image', 600, 400)
    cv2.waitKey(50000)







