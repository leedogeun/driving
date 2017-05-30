import matplotlib.pyplot as plt  # matplotlib
import cv2  # opencv-python
from PIL import Image  # Pillow
import wx #wxPython


##### 이미지 촬영 ################################
def getImage():

    app = wx.App()
    screen = wx.ScreenDC()

    x1, y1 = 0, 0
    x2, y2 = 1000, 550

    bmp = wx.Bitmap(x2, y2)
    mem = wx.MemoryDC(bmp)
    mem.Blit(x1, y1, x2, y2, screen, 0, 0)
    del mem

    bmp.SaveFile('img.bmp', wx.BITMAP_TYPE_BMP)
    img = cv2.imread("img.bmp")

    return img
