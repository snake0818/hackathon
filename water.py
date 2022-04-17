import requests
import json
def get_data(Num = "1007", num = "0"):
    data = "O-A0002-001"
    token = "CWB-F92136A9-0AA3-4E52-8C2B-95B598005F6E"
    Type = "JSON"
    NumOfData = int(Num)+int(num)
    From = int(num)/2

    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/"+data+"?Authorization="+token+"&limit="+str(NumOfData)+"&offset="+str(From)+"&format="+Type
    
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)

        for i in range(int(num),NumOfData):
            print(i)

            dataBase = data["records"]["location"][i]

            location = dataBase["locationName"]
            obstime = dataBase["time"]["obsTime"]
            weather_elements = dataBase["weatherElement"]
            weather_parameters = dataBase["parameter"]
            
            Elev = weather_elements[0]["elementValue"]
            hour1 = weather_elements[1]["elementValue"]
            hour24 = weather_elements[6]["elementValue"]
            City = weather_parameters[0]["parameterValue"]
            citySN = weather_parameters[1]["parameterValue"]
            Town = weather_parameters[2]["parameterValue"]
            townSN = weather_parameters[3]["parameterValue"]
            Attribute = weather_parameters[4]["parameterValue"]

            if hour1 == '-998.00' or hour1 == '0.00':
                hour1 = '無資料'
            if hour24 == '-998.00' or hour24 == '0.00':
                hour24 = '無資料'

            print(location+'  '+obstime+'  '+Elev+' 公尺')
            print('縣市/鄉鎮: '+City+'/'+Town+'  編號:'+citySN+'/'+townSN)
            print('每小時: '+hour1+' 毫米')
            print('日雨量: '+hour24+' 毫米')
            print('自動站屬性: '+Attribute)
            print('--------------------------------------')
        
    else:
        print("Error!")
        print("404 not found")
        print("Can't get data!")


Num = input("欲取得資料數(1~1186): ")
num = input("從第幾筆資料開始: ")
get_data(Num,num)