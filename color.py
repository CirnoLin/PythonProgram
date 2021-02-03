'''Color Dection Ver 0.2 2021/01/27 Edit by 10498
    1.运行需调用电脑摄像头
    2.运行需安装opencv
        操作流程：1）开始菜单找到Anaconda，打开Anaconda prompt
        2）输入 pip install opencv-contrib-python
        3）等待安装完成
    3.暂时对红色和黑色识别准确，此外灰色、橙色、绿色、黄色、白色数据也在文件中，
            删除代码中 “#” 即可进行识别
            （orange颜色识别会受白平衡影响，结果很差，误用！）
'''
 


import numpy as np
import cv2
font = cv2.FONT_HERSHEY_SIMPLEX
lower_green = np.array([35, 110, 106])  
upper_green = np.array([77, 255, 255]) 
 
lower_grey = np.array([0, 0, 46])
upper_grey = np.array([180, 43, 220]) 

upper_white = np.array([180, 30, 255])
lower_white = np.array([0, 0, 221])  

lower_red = np.array([0, 127, 128])
upper_red = np.array([10, 255, 255])

lower_orange = np.array([11, 43, 46])
upper_orange = np.array([25, 255, 255])

lower_yellow = np.array([26, 43, 46])
upper_yellow = np.array([34, 255, 255])

lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 46])

cap = cv2.VideoCapture(0)
if (cap.isOpened()):  
    flag = 1
else:
    flag = 0
num = 0
if (flag):
    while (True):
        ret, frame = cap.read()  
       
        if ret == False:  
            break
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask_red = cv2.inRange(hsv_img, lower_red, upper_red)
        #mask_grey = cv2.inRange(hsv_img, lower_grey, upper_grey)
        #mask_white = cv2.inRange(hsv_img, lower_white, upper_white)
        #mask_orange = cv2.inRange(hsv_img, lower_orange, upper_orange)
        #mask_yellow = cv2.inRange(hsv_img, lower_yellow, upper_yellow)
        mask_black = cv2.inRange(hsv_img, lower_black, upper_black)
          
        mask_red = cv2.medianBlur(mask_red, 7)  
        #mask_grey = cv2.medianBlur(mask_grey, 7) 
        #mask_white = cv2.medianBlur(mask_white, 7) 
        #mask_orange = cv2.medianBlur(mask_orange, 7) 
        #mask_yellow = cv2.medianBlur(mask_yellow, 7) 
        mask_black = cv2.medianBlur(mask_black, 7)
        
        mask = cv2.bitwise_or(mask_red, mask_black)

        contours2, hierarchy2 = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        #contours3, hierarchy = cv2.findContours(mask_grey, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        #contours4, hierarchy = cv2.findContours(mask_white, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        #contours5, hierarchy = cv2.findContours(mask_orange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        #contours6, hierarchy = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        contours7, hierarchy = cv2.findContours(mask_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        

        for cnt2 in contours2:
            (x2, y2, w2, h2) = cv2.boundingRect(cnt2)
            cv2.rectangle(frame, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 255), 2)
            cv2.putText(frame, "Red", (x2, y2 - 5), font, 0.7, (0, 0, 255), 2)
        #for cnt3 in contours3:
            #(x3, y3, w3, h3) = cv2.boundingRect(cnt3)
            #cv2.rectangle(frame, (x3, y3), (x3 + w3, y3 + h3), (0, 255, 255), 2)
            #cv2.putText(frame, "Grey", (x3, y3 - 5), font, 0.7, (0, 255, 0), 2)
        #for cnt4 in contours4:
            #(x4, y4, w4, h4) = cv2.boundingRect(cnt4)
            #cv2.rectangle(frame, (x4, y4), (x4 + w4, y4 + h4), (0, 255, 255), 2)
            #cv2.putText(frame, "Green", (x4, y4 - 5), font, 0.7, (0, 255, 0), 2) 
        #for cnt5 in contours5:
            #(x5, y5, w5, h5) = cv2.boundingRect(cnt5)
            #cv2.rectangle(frame, (x5, y5), (x5 + w5, y5 + h5), (0, 255, 255), 2)
            #cv2.putText(frame, "Orange/Brown", (x5, y5 - 5), font, 0.7, (0, 255, 0), 2)
        #for cnt6 in contours6:
            #(x6, y6, w6, h6) = cv2.boundingRect(cnt6)
            #cv2.rectangle(frame, (x6, y6), (x6 + w6, y6 + h6), (0, 255, 255), 2)
            #cv2.putText(frame, "Yellow", (x6, y6 - 5), font, 0.7, (0, 255, 0), 2)
        for cnt7 in contours7:
            (x7, y7, w7, h7) = cv2.boundingRect(cnt7)
            cv2.rectangle(frame, (x7, y7), (x7 + w7, y7 + h7), (0, 255, 255), 2)
            cv2.putText(frame, "Black", (x7, y7 - 5), font, 0.7, (0, 255, 0), 2)
        num = num + 1
        cv2.imshow("dection", frame)
        cv2.imwrite("imgs/%d.jpg"%num, frame)
        if cv2.waitKey(20) & 0xFF == 27:
            break
cv2.waitKey(0)
cv2.destroyAllWindows()