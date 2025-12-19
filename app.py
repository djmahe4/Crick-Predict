import os
import streamlit as st
import json
from cricket_workflow import matches, get_player_stats, get_player_match_count
from numerology import main as numer
from datetime import datetime
from debug import debug
import pandas as pd
def reset():
    st.session_state.match=None
    st.session_state.playerd={'player':[],'prev':[],'today':[],'tom':[],'dream':[]}
    st.session_state.url=None
    st.session_state.names = {}
def data_down():
    # Initialize session state if not exists
    if 'playerd' not in st.session_state:
        st.session_state.playerd = {'player':[],'prev':[],'today':[],'tom':[],'dream':[]}
    if 'url' not in st.session_state:
        st.session_state.url = None
    if 'names' not in st.session_state:
        st.session_state.names = {}
    if 'match' not in st.session_state:
        st.session_state.match = None
    
    if st.session_state.playerd!={'player':[],'prev':[],'today':[],'tom':[],'dream':[]}:
        st.write("/".join(st.session_state.url.split("/")[:-1]) + "/match-impact-player")
        try:
            st.write(st.session_state.names)
            x=pd.read_html("/".join(st.session_state.url.split("/")[:-1]) + "/match-impact-player")[0]
            st.dataframe(x)
            first11=x.head(11)['Player']
            checker=[st.session_state.names[player] for player in first11]
            y=pd.DataFrame(st.session_state.playerd)
            y['dream']=y['player'].isin(checker)
            edit = st.data_editor(y)
            st.download_button("Download", edit.to_csv(), file_name=f"{st.session_state.match}.csv")
        except Exception as e:
            st.error(f"{e}: MVP List not found!")
            edit=st.data_editor(pd.DataFrame(st.session_state.playerd))
            st.download_button("Download",edit.to_csv(),file_name=f"{st.session_state.match}.csv")
    else:
        st.error("Select match and start to get biorythm values!!")
def player_stats():
    """Page to view player statistics."""
    st.title("🏏 Player Statistics")
    st.write("Get detailed statistics for any cricket player")
    
    player_url = st.text_input(
        "Enter Player Profile URL",
        placeholder="https://www.espncricinfo.com/cricketers/player-name-12345",
        help="Enter the full ESPN Cricinfo player profile URL"
    )
    
    if st.button("Get Player Stats"):
        if player_url:
            with st.spinner("Fetching player statistics..."):
                try:
                    stats = get_player_stats(player_url)
                    match_count = get_player_match_count(player_url)
                    
                    if stats:
                        st.success(f"Statistics for {stats.get('name', 'Player')}")
                        
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.subheader("Basic Information")
                            st.write(f"**Name:** {stats.get('name', 'N/A')}")
                            st.write(f"**Country:** {stats.get('country', 'N/A')}")
                            st.write(f"**Playing Role:** {stats.get('playingRole', 'N/A')}")
                            
                            if stats.get('dateOfBirth'):
                                dob = stats['dateOfBirth']
                                if isinstance(dob, dict):
                                    st.write(f"**Date of Birth:** {dob.get('date', 'N/A')}/{dob.get('month', 'N/A')}/{dob.get('year', 'N/A')}")
                                else:
                                    st.write(f"**Date of Birth:** {dob}")
                        
                        with col2:
                            st.subheader("Playing Style")
                            st.write(f"**Batting Style:** {stats.get('battingStyle', 'N/A')}")
                            st.write(f"**Bowling Style:** {stats.get('bowlingStyle', 'N/A')}")
                        
                        st.divider()
                        st.subheader("Match Statistics")
                        if match_count.get('recent_matches'):
                            st.write(f"**Recent Matches:** {match_count['recent_matches']}")
                        else:
                            st.info("Detailed match statistics not available")
                            
                    else:
                        st.error("Could not retrieve player statistics. Please check the URL.")
                except Exception as e:
                    st.error(f"Error fetching player stats: {e}")
        else:
            st.warning("Please enter a player profile URL")

def app():
    # Initialize session state
    if 'match' not in st.session_state:
        st.session_state.match = None
    if 'playerd' not in st.session_state:
        st.session_state.playerd = {'player':[],'prev':[],'today':[],'tom':[],'dream':[]}
    if 'url' not in st.session_state:
        st.session_state.url = None
    if 'names' not in st.session_state:
        st.session_state.names = {}
    
    # Streamlit UI
    st.title("Dream11 Cricket")
    st.write(datetime.now())
    #st.write(":red[Warning!Local time and time of the website may vary, verify the match dates carefully]")
    
    try:
        contents = matches()
    except Exception as e:
        st.error(f"Error fetching matches: {e}")
        st.info("Please check your internet connection and try again.")
        return
    #file=open("leagues.json","r",encoding="utf-8")
    #contents=json.load(file)
    #file.close()
    
    if not contents:
        st.warning("No matches available at the moment.")
        return
    
    choices = contents
    #print(choices)
    choice = st.selectbox("Match", list(choices.keys()))
    print(choice)
    print()
    match_url=choices[choice]
    st.write(f"Selected match: {choice}")
    st.write(f"Match URL: {match_url}")
    types_of_analysis=["numerology"]
    choice2=st.selectbox("Analysis Type",types_of_analysis)
    if st.button("Start"):
        st.session_state.url=match_url
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
    pg=st.navigation([
        st.Page(app, title="App", icon="🏏"),
        st.Page(player_stats, title="Player Stats", icon="📊"),
        st.Page(debug, title="Learn", icon="🎓"),
        st.Page(data_down, title="Data", icon="ℹ")
    ])
    pg.run()
