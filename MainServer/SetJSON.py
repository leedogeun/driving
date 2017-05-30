import json


##### JSON 데이터 생성 #######################
def setJSON(center, screenCenter, centerStatus):

    carInfo = {                             # JSON 데이터 생성
                  'screenCenter': screenCenter
                , 'center': center
                , 'centerStatus': centerStatus
    }

    jsonString = json.dumps(carInfo, indent=4) # 데이터 JSON 변환

    data = bytes(jsonString, "utf-8")

    return data
