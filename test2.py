import time

import requests,json
import streamlit as st
#from icecream import ic
from bs4 import BeautifulSoup
import http.client
import json
from urllib.parse import urlparse
import re
from icecream import ic

def just_test(url='https://www.espncricinfo.com/series/icc-champions-trophy-2024-25-1459031/pakistan-vs-new-zealand-1st-match-group-a-1466414/live-cricket-score'):
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    so = json.loads(soup.find("script", attrs={'id':'__NEXT_DATA__'}).contents[0])
    with open("data.json" ,"w") as file:
        js=json.dumps(so,indent=2)
        file.write(js)
    #ic(so)
def just_test3(url='https://www.espncricinfo.com/series/csa-4-day-series-division-1-2024-25-1444755/dolphins-vs-western-province-1st-match-1444880/match-playing-xi'):
    data=scraper(url)
    soup = BeautifulSoup(data, "html.parser")
    so = json.loads(soup.find("script", attrs={'id':'__NEXT_DATA__'}).contents[0])
    with open("data.json" ,"w") as file:
        js=json.dumps(so,indent=2)
        file.write(js)
    #ic(so)
def just_test2(url='https://www.espncricinfo.com/cricketers/mitchell-santner-502714'):
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    so = json.loads(soup.find("script", attrs={'id':'__NEXT_DATA__'}).contents[0])
    with open("data.json" ,"w") as file:
        js=json.dumps(so,indent=2)
        file.write(js)
    #ic(so)
    try:
        return so['props']['appPageProps']['data']['player']['fullName'], so['props']['appPageProps']['data']['player']['dateOfBirth']
    except:
        return None
#just_test2()
#just_test()
def get_dat():
    with open("data.json",'r') as file:
        js=json.loads(file.read())
        #ic(js,type(js))
    #ic(js.keys())
    #ic(js['props']['appPageProps'])
    with open("main.json",'w') as file:
        njs=json.dumps(js['props']['appPageProps'],indent=2)
        file.write(njs)
def get_dat2():
    url='https://www.espncricinfo.com/series/icc-champions-trophy-2024-25-1459031/pakistan-vs-new-zealand-1st-match-group-a-1466414/live-cricket-score'
    id=url.split("/")[-2].split("-")[-1]
    with open("main.json", 'r') as file:
        js = json.loads(file.read())
    #for j in js['data']['data']:
    #ic(js['data']['data']['match'].keys())
    try:
        if js['data']['data']['match']['objectId'] == int(id):
            for i in js['data']['data']['match']:
                #ic(i, js['data']['data']['match'][i])
                return js['data']['data']['match']['startTime'],js['data']['data']['match']['ground']['town']['timezone']
    except KeyError:
        return
def get_dat4(url='https://www.espncricinfo.com/cricketers/yaseen-vallie-327831'):
    data=scraper(url)
    soup = BeautifulSoup(data, "html.parser")
    so = json.loads(soup.find("script", attrs={'id': '__NEXT_DATA__'}).contents[0])
    #ic(so['props']["appPageProps"]["data"]['player'].keys())
    #ic(so['props']["appPageProps"]["data"]['player']['dateOfBirth'],so['props']["appPageProps"]["data"]['player']['fullName'])

#print(get_dat2())
def get_loc(url='https://www.espncricinfo.com/series/icc-champions-trophy-2024-25-1459031/pakistan-vs-new-zealand-1st-match-group-a-1466414/live-cricket-score'):
    data=scraper(url)
    soup = BeautifulSoup(data, "html.parser")
    so = json.loads(soup.find("script", attrs={'id': '__NEXT_DATA__'}).contents[0])
    #id = url.split("/")[-2].split("-")[-1]
    return so['props']['appPageProps']['data']['data']['match']['startTime'],so['props']['appPageProps']['data']['data']['match']['ground']['town']['timezone']
#print(get_loc())

def scraper(url):
    #url =
    #ic(url)
    parsed = urlparse(url)
    conn = http.client.HTTPSConnection(parsed.netloc)
    conn.request("GET", parsed.path)
    res = conn.getresponse()
    data = res.read()
    #ic(data)
    return data
    details = json.loads(data.decode("utf-8"))
    #ic(details.keys())
    return details
def matches(url='https://www.espncricinfo.com/live-cricket-match-schedule-fixtures'):

    data=scraper(url)
    soup = BeautifulSoup(data, "html.parser")
    so = json.loads(soup.find("script", attrs={'id':'__NEXT_DATA__'}).contents[0])
    #with open("data.json" ,"w") as file:
        #js=json.dumps(so,indent=2)
        #file.write(js)
    #ic(so)
    mids={}
    for i in so['props']['appPageProps']['data']['data']['content']['matches']:
        mids.update({f"{i['teams'][0]['team']['name']} vs {i['teams'][1]['team']['name']}":f"https://www.espncricinfo.com/series/{i['series']['slug']}-{i['series']['objectId']}/{i['slug']}-{i['objectId']}/live-cricket-score"})

    #ic(mids)
    return mids
def match11sub(url):
    #global st
    data=scraper(url)
    #ic(data)
    dic={}
    soup = BeautifulSoup(data, "html.parser")
    so = json.loads(soup.find("script", attrs={'id': '__NEXT_DATA__'}).contents[0])
    for player in so['props']["appPageProps"]["data"]["content"]["matchPlayers"]["teamPlayers"][0]['players']:
        dic.update({player["player"]["longName"]:f"https://www.espncricinfo.com/cricketers/{player['player']['slug']}-{player['player']['objectId']}"})
    for player in so['props']["appPageProps"]["data"]["content"]["matchPlayers"]["teamPlayers"][1]['players']:
        dic.update({player["player"]["longName"]:f"https://www.espncricinfo.com/cricketers/{player['player']['slug']}-{player['player']['objectId']}"})

    return dic

def match11(url='https://www.espncricinfo.com/series/csa-4-day-series-division-1-2024-25-1444755/dolphins-vs-western-province-1st-match-1444880/full-scorecard',cond="match-playing-xi"):
    #global st
    urll=url.split("/")
    urll[-1]=cond
    url="/".join(urll)
    playerd=match11sub(url)
    print(playerd)
    if playerd == {} and cond=="match-squads":
        st.write("Squads not available")
        raise "Squad not found"
    elif playerd=={}:
        print("Lineup not available")
        playerd=match11(url,"match-squads")
    urll[-1]='live-cricket-score'
    nurl="/".join(urll)
    mdate=get_loc(nurl)
    #ic(playerd,mdate)
    return playerd,mdate
def get_bdata(players={'Andile Simelane': 'https://www.espncricinfo.com/cricketers/andile-simelane-1070754',
              'Beuran Hendricks': 'https://www.espncricinfo.com/cricketers/beuran-hendricks-379927',
              'Daniel Smith': 'https://www.espncricinfo.com/cricketers/daniel-smith-946453',
              'Daryn Dupavillon': 'https://www.espncricinfo.com/cricketers/daryn-dupavillon-501907',
              'Edward Moore': 'https://www.espncricinfo.com/cricketers/edward-moore-481975',
              'George Linde': 'https://www.espncricinfo.com/cricketers/george-linde-481875',
              'Jason Smith': 'https://www.espncricinfo.com/cricketers/jason-smith-498582',
              'Jonathan Bird': 'https://www.espncricinfo.com/cricketers/jonathan-bird-696587',
              'Kyle Simmonds': 'https://www.espncricinfo.com/cricketers/kyle-simmonds-550251',
              'Marques Ackerman': 'https://www.espncricinfo.com/cricketers/marques-ackerman-596436',
              'Mihlali Mpongwana': 'https://www.espncricinfo.com/cricketers/mihlali-mpongwana-948593',
              'Mthiwekhaya Nabe': 'https://www.espncricinfo.com/cricketers/mthiwekhaya-nabe-977991',
              'Okuhle Cele': 'https://www.espncricinfo.com/cricketers/okuhle-cele-595618',
              'Prenelan Subrayen': 'https://www.espncricinfo.com/cricketers/prenelan-subrayen-437438',
              'Romashan Pillay': 'https://www.espncricinfo.com/cricketers/romashan-pillay-1385638',
              'Sarel Erwee': 'https://www.espncricinfo.com/cricketers/sarel-erwee-324260',
              'Sean Whitehead': 'https://www.espncricinfo.com/cricketers/sean-whitehead-595283',
              'Slade van Staden': 'https://www.espncricinfo.com/cricketers/slade-van-staden-1070762',
              'Tshepang Dithole': 'https://www.espncricinfo.com/cricketers/tshepang-dithole-488998',
              'Valentine Kitime': 'https://www.espncricinfo.com/cricketers/valentine-kitime-946351',
              'Wesley Bedja': 'https://www.espncricinfo.com/cricketers/wesley-bedja-1412823',
              'Yaseen Vallie': 'https://www.espncricinfo.com/cricketers/yaseen-vallie-327831'}):
    bdata={}
    for player in players:
        with st.spinner(f"Getting bdata of {player}"):
            time.sleep(1)
            data=scraper(players[player])
            soup = BeautifulSoup(data, "html.parser")
            so = json.loads(soup.find("script", attrs={'id': '__NEXT_DATA__'}).contents[0])
            bdata.update({so['props']["appPageProps"]["data"]['player']['fullName']:so['props']["appPageProps"]["data"]['player']['dateOfBirth']})
            st.session_state.names.update({so['props']["appPageProps"]["data"]['player']['longName']:so['props']["appPageProps"]["data"]['player']['fullName']})
            #ic(so['props']["appPageProps"]["data"]['player']['longName'],so['props']["appPageProps"]["data"]['player']['name'])
    #ic(bdata)
    return bdata
#get_bdata()
#match11()
#get_dat4()

    #ic(bdata)
def tester():
    data = scraper("https://www.espncricinfo.com/cricketers/shikha-pandey-442145")
    soup = BeautifulSoup(data, "html.parser")
    so = json.loads(soup.find("script", attrs={'id': '__NEXT_DATA__'}).contents[0])

    ic(so['props']["appPageProps"]["data"]['player'])
# ic(bdata)
#tester()