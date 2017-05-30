import socket
import threading
import json
import keyInput


##### 클라이언트 IP, PORT 설정 ##########################
HOST = "192.168.35.91"
PORT = 10000


##### 소켓 생성 및 서버 연결 ##########################
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


##### 데이터 수신 ##########################
def getData():

    while True:
        data = s.recv(1024)

        if not data:
            break

        else:

            try:
                data = data.decode("utf-8","ignore")

                data = json.loads(data)

                print(data)

                keyInput.keyInput(data['centerStatus'])

            except:
                pass

    s.close()


threading._start_new_thread(getData,())


##### 반복 수행 ##########################
while True:
    pass
