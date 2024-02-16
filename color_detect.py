#不可用于商用#

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# 默认设置摄像头分辨率为（1280，720）
# 如果感觉图像卡顿严重，可以降低为（640，320）
cap.set(3, 1280)
cap.set(4, 720)

# 设置红色的阙值
red_lower = np.array([0,76,88])
red_upper = np.array([179,255,255])

while 1:
    # ret为是否找到图像， frame是帧本身
    ret, frame = cap.read()
    frame = cv2.imread("F://3150.jpg")#测试代码是读取图片，如果要读取视频流可以将该句注释
    #frame = cv2.GaussianBlur(frame, (5, 5), 0)  # 高斯模糊
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # 转hsv
    mask = cv2.inRange(hsv, red_lower, red_upper)  # 生成掩膜
    cv2.namedWindow("capture0", cv2.WINDOW_NORMAL);
    cv2.resizeWindow("capture0", 640, 480);
    cv2.imshow('capture0', mask)
    # 形态学操作
    mask = cv2.erode(mask, None, iterations=2)#腐蚀操作，值越大腐蚀越严重，使图像中的高亮区逐渐减小
    mask = cv2.dilate(mask, None, iterations=2)#膨胀操作，使图像中的高亮区域逐渐增长
    mask = cv2.GaussianBlur(mask, (3, 3), 0)
    res = cv2.bitwise_and(frame, frame, mask=mask)  # 与运算
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]  # 检测颜色的轮廓
    if len(cnts) > 0:
        cnt = max(cnts, key=cv2.contourArea)#按照面积最大的方法来求最大轮廓
        (x, y), radius = cv2.minEnclosingCircle(cnt) #获得轮廓外接圆的圆心坐标与半径
        cv2.circle(frame, (int(x), int(y)), int(radius) ,
                   (255, 0, 255), 2)  # 找到后在每个轮廓上画圆
        print('x:', x, 'y:', y)
    cv2.namedWindow("capture", cv2.WINDOW_NORMAL);
    cv2.resizeWindow("capture", 640, 480);
    cv2.imshow('capture', frame)
    if cv2.waitKey(1) == 27:  #esc退出
        break
#cap.release()
cv2.destroyAllWindows()
