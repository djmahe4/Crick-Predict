import os
#os.popen("pip install -r requirements.txt")
import streamlit as st
import requests
import json
##
from test import *
from numerology import main as numer
from datetime import datetime
from debug import debug
def app():
    # Streamlit UI
    st.title("Dream11 Cricket")
    st.write(datetime.now())
    st.write(":red[Warning!Local time and time of the website may vary, verify the match dates carefully]")
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
            numer(match_url)
if __name__=="__main__":
    pg=st.navigation([st.Page(app,title="App",icon="🏏"),st.Page(debug,title="Learn",icon="🎓")])
    pg.run()