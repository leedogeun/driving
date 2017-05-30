import numpy as np  # numpy
import cv2  # opencv-python


##### 이미지 와핑 (탑뷰) ########################
def imageWarping(img):

    ##### 좌표 설정 ############################
    preX1, preY1    =  450, 450
    preX2, preY2    =  100, 550
    preX3, preY3    =  780, 450
    preX4, preY4    = 1000, 550

    postX1, postY1  =  100,   0
    postX2, postY2  =  100, 550
    postX3, postY3  = 1000,   0
    postX4, postY4  = 1000, 550

    prePoint = np.float32([
          [preX1, preY1]
        , [preX2, preY2]
        , [preX3, preY3]
        , [preX4, preY4]
    ])

    postPoint = np.float32([
          [postX1, postY1]
        , [postX2, postY2]
        , [postX3, postY3]
        , [postX4, postY4]
    ])

    ##### 이미지 와핑 ##########################
    M = cv2.getPerspectiveTransform(prePoint, postPoint)
    dst = cv2.warpPerspective(img, M, (postX4, postY4))

    ##### 썸네일 생성 #########################
    thumbRate = 4
    thumbWidth = int(postX4 / thumbRate)
    thumbHeight = int(postY4 / thumbRate)
    thumbnail = cv2.resize(dst, (thumbWidth, thumbHeight))

    ##### 이미지 출력 #########################
    cv2.imshow("img", thumbnail)
    return thumbnail
