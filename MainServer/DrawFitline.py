import cv2  # opencv-python


##### 대표선 그리기 ####################################
def draw_fit_line(img, f_lines):
    try:

        x1, y1 = f_lines[0], f_lines[1]
        x2, y2 = f_lines[2], f_lines[3]

        lineColor = (255, 255, 0)
        lineWeight = 5

        cv2.line(img, (x1, y1), (x2, y2), lineColor, lineWeight)

    except:
        pass
