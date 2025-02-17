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
import pandas as pd
def reset():
    st.session_state.match=None
    st.session_state.playerd={'player':[],'prev':[],'today':[],'tom':[],'dream':[]}
def data_down():
    if st.session_state.playerd!={'player':[],'prev':[],'today':[],'tom':[],'dream':[]}:
        edit=st.data_editor(pd.DataFrame(st.session_state.playerd))
        st.download_button("Download",edit.to_csv(),file_name=f"{st.session_state.match}.csv")
    else:
        st.error("Select match and start to get biorythm values!!")
def app():
    # Streamlit UI
    st.title("Dream11 Cricket")
    st.write(datetime.now())
    #st.write(":red[Warning!Local time and time of the website may vary, verify the match dates carefully]")
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
    choice2=st.selectbox("Analysis Type",types_of_analysis)
    if st.button("Start"):
        st.session_state.match = choice
        st.write(f"Selected analysis type: {choice2}")
        print(choice2)
        if choice2=="numerology":
            numer(match_url)
    if st.button("Reset"):
        reset()
        if st.session_state.match==None:
            st.success("Cleared!")
if __name__=="__main__":
    if "match" not in st.session_state:
        st.session_state.match=None
    if 'playerd' not in st.session_state:
        st.session_state.playerd={'player':[],'prev':[],'today':[],'tom':[],'dream':[]}
    pg=st.navigation([st.Page(app,title="App",icon="🏏"),st.Page(debug,title="Learn",icon="🎓"),
                      st.Page(data_down,title="Data",icon="ℹ")])
    pg.run()
