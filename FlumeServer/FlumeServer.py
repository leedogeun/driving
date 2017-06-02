import socket
import threading
import json
import Dao


##### 클라이언트 IP, PORT 설정 ##########################
HOST = "192.168.35.90"
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

                screenCenter = str(data['screenCenter'])
                center       = str(data['center'])
                centerStatus = str(data['centerStatus'])
                keyValue     = str(data['keyValue'])

                carLogInfo = open("/home/pilot-pjt/working/cat-batch-log/carLogInfo.txt", "a")
                carLogInfo.write( screenCenter + ","
                                + center       + ","
                                + centerStatus + ","
                                + keyValue     + "\n"
                )
                carLogInfo.close()

                Dao.insertDao( screenCenter
                             , center
                             , centerStatus
                             , keyValue
                )

            except:
                pass

    s.close()


threading._start_new_thread(getData,())


##### 반복 수행 ##########################
while True:
    pass
