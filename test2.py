import requests,json
from icecream import ic
from bs4 import BeautifulSoup

def just_test(url='https://www.espncricinfo.com/series/icc-champions-trophy-2024-25-1459031/pakistan-vs-new-zealand-1st-match-group-a-1466414/live-cricket-score'):
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    so = json.loads(soup.find("script", attrs={'id':'__NEXT_DATA__'}).contents[0])
    with open("data.json" ,"w") as file:
        js=json.dumps(so,indent=2)
        file.write(js)
    ic(so)
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
just_test2()
#just_test()
def get_dat():
    with open("data.json",'r') as file:
        js=json.loads(file.read())
        #ic(js,type(js))
    ic(js.keys())
    ic(js['props']['appPageProps'])
    with open("main.json",'w') as file:
        njs=json.dumps(js['props']['appPageProps'],indent=2)
        file.write(njs)
def get_dat2():
    url='https://www.espncricinfo.com/series/icc-champions-trophy-2024-25-1459031/pakistan-vs-new-zealand-1st-match-group-a-1466414/live-cricket-score'
    id=url.split("/")[-2].split("-")[-1]
    with open("main.json", 'r') as file:
        js = json.loads(file.read())
    #for j in js['data']['data']:
    ic(js['data']['data']['match'].keys())
    try:
        if js['data']['data']['match']['objectId'] == int(id):
            for i in js['data']['data']['match']:
                ic(i, js['data']['data']['match'][i])
                return js['data']['data']['match']['startTime'],js['data']['data']['match']['ground']['town']['timezone']
    except KeyError:
        return
#print(get_dat2())
def get_loc(url='https://www.espncricinfo.com/series/icc-champions-trophy-2024-25-1459031/pakistan-vs-new-zealand-1st-match-group-a-1466414/live-cricket-score'):
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    so = json.loads(soup.find("script", attrs={'id': '__NEXT_DATA__'}).contents[0])
    #id = url.split("/")[-2].split("-")[-1]
    return so['props']['appPageProps']['data']['data']['match']['startTime'],so['props']['appPageProps']['data']['data']['match']['ground']['town']['timezone']
#print(get_loc())