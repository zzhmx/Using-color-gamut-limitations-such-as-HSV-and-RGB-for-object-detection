#不可用于商用#

import cv2
import numpy as np
def getROI(event, x, y, flags, param):
    global ix, iy, drawing, img, hsv_img, hsv_roi, box ,img2
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img2=img.copy()
            cv2.rectangle(img2, (ix, iy), (x, y), (0, 255, 0), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        box = (min(ix,x), min(iy,y), abs(ix-x), abs(iy-y))
        roi = hsv_img[box[1]:box[1]+box[3], box[0]:box[0]+box[2], :]
        h_min, s_min, v_min = np.min(roi, axis=(0,1))
        h_max, s_max, v_max = np.max(roi, axis=(0,1))
        print("Hue: ", h_min, h_max)
        print("Saturation: ", s_min, s_max)
        print("Value: ", v_min, v_max)
        #cv2.imshow("ROI", roi)
        hsv_roi[:] = (h_min, s_min, v_min), (h_max, s_max, v_max)
        img2=img.copy()
# 读取图像
img = cv2.imread("3151.jpg")
cap = cv2.VideoCapture(0)
while 1:
    # ret为是否找到图像， frame_cap是帧本身
    ret, frame_cap = cap.read()
    if ret:
        cv2.namedWindow("cap", 0);
        cv2.resizeWindow("cap", 1080, 720);
        cv2.imshow('cap', frame_cap)
        if cv2.waitKey(1) == ord(' '): #按下空格截下当前帧用于读取色域范围
            img=frame_cap
            cv2.destroyAllWindows()
            cap.release()
            break
        elif cv2.waitKey(1) == ord('q'): #按下字母q使用默认图片用于读取色域范围
            cv2.destroyAllWindows()
            cap.release()
            break
img2=img.copy()
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv_roi = np.zeros((1, 2, 3))
# 定义窗口并绑定事件
cv2.namedWindow("image",0)
cv2.resizeWindow("image", 640, 480)
cv2.setMouseCallback("image", getROI)
drawing = False
# 循环显示图像
while True:
    cv2.imshow("image", img2)
    k = cv2.waitKey(1) & 0xFF
    if cv2.waitKey(1) == 27:  # esc退出
        break
# 释放资源
cv2.destroyAllWindows()
