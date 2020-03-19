import requests
from bs4 import BeautifulSoup
import json

URL = "https://summit.fossasia.org/event/schedule.html#"

def scrap ():
    req = requests.get(URL)
    soup = BeautifulSoup(req.content, "html.parser")
    links = soup.findAll("a")
    track_names = []
    room_names = []
    
    for link in links:
        if link.has_attr("class"):
            # print(link["class"])
            if "track-name" in link["class"]:
                track_names.append(link.text)
            if "room-name" in link["class"]:
                room_names.append(link.text)

    with open("TrackNames.json", "w") as tracknames_file:tracknames_file.write(json.dumps(track_names))
    with open("RoomNames.json", "w") as roomnames_file:roomnames_file.write(json.dumps(room_names))


    def get_session (date):
        session = []
        session_info = soup.find("div", {"class":date}).findAll("div", {"class":"time-filter"})
        for event in session_info:
            time = event.find("div", {"class":"eventtime"}).text
            title = event.find("div", {"class":"margin-down-15"}).text
            info = event.findAll("ul", {"class":"speaker-name-list"})
            speakers = info[0].text
            session_type = info[1].text
            session.append({"Title": title,
                            "Time": time,
                            "Speakers": speakers.replace("\u00a0",""),
                            "SessionType": session_type})
        return session
    
    march19 = get_session("2020-03-19")
    march20 = get_session("2020-03-20")
    march21 = get_session("2020-03-21")
    
    with open("March19.json", "w") as march19_file:march19_file.write(json.dumps(march19))
    with open("March20.json", "w") as march19_file:march19_file.write(json.dumps(march20))
    with open("March21.json", "w") as march19_file:march19_file.write(json.dumps(march21))

    
    print("OK")
    

# main
scrap()
