import socket
import threading
import json
import GetImage
import ImageWarping
import GetHoughLines
import KeyInput
import SetJSON


##### 서버 IP, PORT 설정 ########################
HOST = '192.168.35.91'
PORT = 10000


##### 소켓 생성 및 서버 오픈 ###########################
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5) # 클라이언트 연결 대기
conn, addr = s.accept() # 클라이언트 연결 수락
print('Connected by', addr)


##### main ###########################################
def main():

    while True:

        img = GetImage.getImage()  # 이미지 추출

        img = ImageWarping.imageWarping(img)  # 탑뷰 조작

        center = GetHoughLines.hough(img, 20)  # 차선 검출하여 센터 설정
        screenCenter = 135
        centerStatus = screenCenter - center

        KeyInput.keyInput(centerStatus)  # 키 조작

        data = SetJSON.setJSON(center, screenCenter, centerStatus) # JSON 데이터 생성

        conn.send(data) # JSON 데이터 전송

    conn.close()


threading._start_new_thread(main,())


while True:
    pass
