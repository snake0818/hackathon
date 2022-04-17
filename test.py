import requests
import json
def get_data():

    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-F92136A9-0AA3-4E52-8C2B-95B598005F6E"
    getType = "&format=json"
    LocationName = "&locationName="

    response = requests.get(url+getType+LocationName)

    if response.status_code == 200:
        #print(response.text)
        data = json.loads(response.text)
        
        location = data["records"]["location"][0]["locationName"]

        weather_elements = data["records"]["location"][0]["weatherElement"]
        start_time = weather_elements[0]["time"][0]["startTime"]
        end_time = weather_elements[0]["time"][0]["endTime"]
        weather_state = weather_elements[0]["time"][0]["parameter"]["parameterName"]
        rain_prob = weather_elements[1]["time"][0]["parameter"]["parameterName"]
        min_tem = weather_elements[2]["time"][0]["parameter"]["parameterName"]
        comfort = weather_elements[3]["time"][0]["parameter"]["parameterName"]
        max_tem = weather_elements[4]["time"][0]["parameter"]["parameterName"]

        print(location)
        print(start_time)
        print(end_time)
        print(rain_prob)
        print(min_tem+'~'+max_tem)
        print(weather_state)
        print(comfort)
        print('--------------------')

    else:
        print("Can't get data!")

get_data()