#不可用于商用#

import cv2
import numpy as np

def nothing(x):
    pass

def Calibrate_size(lower,upper):
    if lower[0]<=upper[0] and lower[1]<=upper[1] and lower[2]<=upper[2] :
        return 1
    else :
        return 0

cap = cv2.VideoCapture(0)
frame = cv2.imread("3151.jpg")

while 1:
    # ret为是否找到图像， frame_cap是帧本身
    ret, frame_cap = cap.read()
    if ret:
        cv2.namedWindow("cap", 0);
        cv2.resizeWindow("cap", 1080, 720);
        cv2.imshow('cap', frame_cap)
        if cv2.waitKey(1) == ord(' '): #按下空格截下当前帧用于色域筛选
            frame=frame_cap
            cv2.destroyAllWindows()
            cap.release()
            break
        elif cv2.waitKey(1) == ord('q'):  #按下q使用自带图片用于色域筛选
            cv2.destroyAllWindows()
            cap.release()
            break
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.resizeWindow("img", 400, 200);
cv2.createTrackbar('H_max','img',179,179,nothing)
cv2.createTrackbar('H_min','img',0,179,nothing)
cv2.createTrackbar('S_max','img',255,255,nothing)
cv2.createTrackbar('S_min','img',0,255,nothing)
cv2.createTrackbar('V_max','img',255,255,nothing)
cv2.createTrackbar('V_min','img',0,255,nothing)
# 将图像转换到 HSV 空间
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
while (1):
    h_max = cv2.getTrackbarPos('H_max', 'img')
    h_min = cv2.getTrackbarPos('H_min', 'img')
    s_max = cv2.getTrackbarPos('S_max', 'img')
    s_min = cv2.getTrackbarPos('S_min', 'img')
    v_max = cv2.getTrackbarPos('V_max', 'img')
    v_min = cv2.getTrackbarPos('V_min', 'img')
    lower_hsv=np.array([h_min,s_min,v_min])
    upper_hsv=np.array([h_max,s_max,v_max])
    if Calibrate_size(lower_hsv, upper_hsv) == 1:
        # 设置阈值图像中只出现hsv范围的物件
        mask = cv2.inRange(hsv, lower_hsv, upper_hsv)#二值
        img_useful = cv2.bitwise_and(frame, frame, mask=mask)  # 与操作
        cv2.namedWindow("capture", cv2.WINDOW_NORMAL);
        cv2.resizeWindow("capture", 1080, 720);
        cv2.imshow('capture', img_useful)
    else :
        print('三个通道最大值需要大于最小值/The maximum value of the three channels needs to be greater than the minimum value')
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break

