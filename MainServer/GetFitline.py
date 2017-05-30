import numpy as np  # numpy
import cv2  # opencv-python


##### 대표선 구하기 ####################################
def get_fitline(img, f_lines):

    try:
        lines = np.squeeze(f_lines)
        lines = lines.reshape(lines.shape[0] * 2, 2)
        rows, cols = img.shape[:2]

        output = cv2.fitLine(lines, cv2.DIST_L2, 0, 0.01, 0.01)

        vx, vy, x, y = output[0], output[1], output[2], output[3]

        x1, y1 = int(((img.shape[0] - 1) - y) / vy * vx + x), img.shape[0] - 1
        x2, y2 = int(((img.shape[0] / 2 + 100) - y) / vy * vx + x), int(img.shape[0] / 2) + 100

        fit_line_arr = [x1, y1, x2, y2]
        fit_slope_degree = (np.arctan2(fit_line_arr[1] - fit_line_arr[3], fit_line_arr[0] - fit_line_arr[2]) * 180) / np.pi  # 기울기 구하기
        fit_slope_degree = np.abs(fit_slope_degree)

        ##### 차선의 기울어진 방향 구하기 #########################
        direction = fit_line_arr[0] - fit_line_arr[2]

        if direction >= 0:   # 우측으로 기울어진 차선의 경우
            x2 = int(np.sqrt(np.power((img.shape[0]/np.sin(fit_slope_degree*(np.pi/180))), 2)-np.power(img.shape[0], 2)) + fit_line_arr[0])
            y2 = 0

        elif direction < 0:  # 좌측으로 기울어진 차선의 경우
            x2 = int(fit_line_arr[0] - np.sqrt(np.power(img.shape[0]/np.sin((180-fit_slope_degree)*(np.pi/180)),2)-np.power(img.shape[0], 2)))
            y2 = 0

        result = [x1, y1, x2, y2]

    except:
        result = None
        pass

    return result
