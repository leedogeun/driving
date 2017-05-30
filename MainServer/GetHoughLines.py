import numpy as np  # numpy
import cv2  # opencv-python
import GetFitline
import DrawFitline


##### 허프 변환 (차선 검출) #######################
def hough(img, thr):
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(imgray, 100, 150, apertureSize=3)

    ##### 차선 검출 #################################
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, thr, minLineLength=4, maxLineGap=20)  # 허프 변환

    ##### 수평선 필터링 ###################################
    line_arr = np.squeeze(lines)

    try:
        slope_degree = (np.arctan2(line_arr[:, 1] - line_arr[:, 3], line_arr[:, 0] - line_arr[:, 2]) * 180) / np.pi  # 기울기 구하기

        line_arr = line_arr[np.abs(slope_degree) < 105]         # 수평 기울기 제한
        slope_degree = slope_degree[np.abs(slope_degree) < 105] # 수평 기울기 제한

        line_arr = line_arr[np.abs(slope_degree) > 75]          # 수직 기울기 제한
        slope_degree = slope_degree[np.abs(slope_degree) > 75]   # 수직 기울기 제한

        line_arr = line_arr[line_arr[:, 0] > 30, :]             # 변두리 선 제거

        ##### 좌측선, 우측선 분류 ####################################
        L_lines = line_arr[line_arr[:, 0] < (img.shape[1]/2)+5, :]
        R_lines = line_arr[line_arr[:, 0] > (img.shape[1]/2)+5, :]

        temp = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)                    # 필터링된 직선 버리기
        L_lines, R_lines = L_lines[:, None], R_lines[:, None]                               # 필터링된 직선 버리기

    except:
        pass

    ##### 대표선 검출 ######################
    try:
        left_fit_line = GetFitline.get_fitline(img, L_lines)   # 좌측 대표선 구하기
        DrawFitline.draw_fit_line(temp, left_fit_line)                  # 좌측 대표선 그리기
        lineImg = cv2.addWeighted(img, 1, temp, 1.0, 0.0)   # 좌측 대표선 그리기

        #print("left : ", left_fit_line)

        cv2.imshow('img', lineImg)

    except:
        pass

    try:
        right_fit_line = GetFitline.get_fitline(img, R_lines) # 우측 대표선 구하기
        DrawFitline.draw_fit_line(temp, right_fit_line)                 # 우측 대표선 그리기
        lineImg = cv2.addWeighted(img, 1, temp, 1.0, 0.0)   # 우측 대표선 그리기

        #print("right : ", right_fit_line)

        cv2.imshow('img', lineImg)

    except:
        pass

    cv2.waitKey(1)

    ##### 센터 검출 ######################
    try:
        if right_fit_line == None:
            center = left_fit_line[0] + 55

        elif left_fit_line == None:
            center = right_fit_line[0] - 55

        else:
            center = int((left_fit_line[0] + right_fit_line[0])/2)

    except:
        center = 135
        pass

    return center
