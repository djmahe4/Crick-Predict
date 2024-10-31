import requests
from bs4 import BeautifulSoup
from time import sleep
import re

def matches():
    response = requests.get('https://www.espncricinfo.com/live-cricket-match-schedule-fixtures')
    #sleep(10)
    rdata={}
    data=response.text
    soup=BeautifulSoup(data,"html.parser")
    #print(element.text)  # or element.get_text()

    # Find all match elements with the class "ds-no-tap-higlight"
    matches = soup.find_all('a', class_='ds-no-tap-higlight') # Extract match names and hrefs
    for match in matches:
        match_name = match.find('p', class_='ds-text-compact-s ds-font-bold ds--mb-1 ds-text-typo').text.strip()
        href = match.get('href')
        print(f"Match: {match_name}, Href: {href}")
        rdata.update({match_name:f"https://www.espncricinfo.com{href}"})
    return rdata
#rdata=matches()
#print(rdata)
def match11sub(url):
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    # Find all player elements with the specified class
    players = soup.find_all('a',
                            class_='ds-inline-flex ds-items-start ds-leading-none')  # Extract player names and hrefs
    playerd = {}
    # match_format = soup.find_all('span', class_='ds-text-tight-s ds-font-regular')#.text.strip()
    # try:
    # match = re.findall(r'\((.*?)\)', match_format[0].text)
    # print(f"Match Format: {match[0]}")
    # except IndexError:
    # print(match_format,"notfound")
    # finally:
    for player in players:
        player_name = player.find('span').text.strip()
        # print(player_name)
        href = player.get('href')
        # print(f"Player: {player_name}, Href: {href}")
        if "cricketers" in href:
            playerd.update({player_name: f"https://www.espncricinfo.com{href}"})
    return playerd
def match11(url='https://www.espncricinfo.com/series/csa-4-day-series-division-1-2024-25-1444755/dolphins-vs-western-province-1st-match-1444880/full-scorecard',cond="match-playing-xi"):
    global st
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
        
    return playerd#,""
print(match11())