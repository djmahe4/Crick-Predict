import requests
from bs4 import BeautifulSoup
import http.client
import json
from urllib.parse import urlparse
from time import sleep
import re,json
#from icecream import ic
import streamlit as st
#rdata=matches()
#print(rdata)
def get_loc(url='https://www.espncricinfo.com/series/icc-champions-trophy-2024-25-1459031/pakistan-vs-new-zealand-1st-match-group-a-1466414/live-cricket-score'):
    data=scraper(url)
    soup = BeautifulSoup(data, "html.parser")
    so = json.loads(soup.find("script", attrs={'id': '__NEXT_DATA__'}).contents[0])
    #id = url.split("/")[-2].split("-")[-1]
    return so['props']['appPageProps']['data']['data']['match']['startTime'],so['props']['appPageProps']['data']['data']['match']['ground']['town']['timezone']
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
    return playerd,mdate
@st.cache_resource
def scraper(url):
    #url =
    #ic(url)
    parsed = urlparse(url)
    conn = http.client.HTTPSConnection(parsed.netloc)
    conn.request("GET", parsed.path)
    res = conn.getresponse()
    data = res.read()
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
def debug_matches(url='https://www.espncricinfo.com/live-cricket-match-results'):

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
#print(match11())
#print(matches())
