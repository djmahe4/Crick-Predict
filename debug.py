import os
#os.popen("pip install -r requirements.txt")
import streamlit as st
import requests
##
import json
from test import debug_matches
from datetime import datetime, timezone
from bs4 import BeautifulSoup
from numerology import main as numer

def debug():
    # Streamlit UI
    st.title("Dream11 Cricket Review")
    st.write(datetime.now())
    #st.write(":red[Warning!Local time and time of the website may vary, verify the match dates carefully]")
    contents=debug_matches()
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
    choice2=st.selectbox("Analysis Type",types_of_analysis)
    if st.button("Start"):
        st.session_state.match = choice
        st.write(f"Selected analysis type: {choice2}")
        print(choice2)
        if choice2=="numerology":
            numer(match_url)
