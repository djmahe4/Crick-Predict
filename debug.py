import os
#os.popen("pip install -r requirements.txt")
import streamlit as st
import requests
import json
from datetime import datetime, timezone
from bs4 import BeautifulSoup
from numerology import main as numer

def matches():#dont get confused it is for debugging last matches
    response = requests.get('https://www.espncricinfo.com/live-cricket-match-results')
    # sleep(10)
    rdata = {}
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    # print(element.text)  # or element.get_text()

    # Find all match elements with the class "ds-no-tap-higlight"
    matches = soup.find_all('div', class_='ds-px-4 ds-py-3')  # Extract match names and hrefs
    for match in matches:
        match_name = match.find('div', class_='ds-flex ds-flex-col ds-mt-2 ds-mb-2').text.strip()
        href=match.find('a', class_='ds-no-tap-higlight').get('href')
        #print(f"Match: {match_name}, Href: {href}")
        rdata.update({match_name: f"https://www.espncricinfo.com{href}"})
    return rdata

# Streamlit UI
st.title("Dream11 Cricket Review")
st.write(datetime.now())
contents=matches()
#file=open("leagues.json","r",encoding="utf-8")
#contents=json.load(file)
#file.close()
choices=contents
#print(choices)
choice=st.selectbox("Match",list(choices.keys()))
print(choice)
print()
match_url=choices[choice]
st.write(f"Selected match: {choice}")
st.write(f"Match URL: {match_url}")
types_of_analysis=["numerology"]
choice=st.selectbox("Analysis Type",types_of_analysis)
if st.button("Start"):
    st.write(f"Selected analysis type: {choice}")
    print(choice)
    if choice=="numerology":
        numer(match_url,st)