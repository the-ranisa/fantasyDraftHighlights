import requests, json, time
from config import *
from vDictSleeper import vDictSleeper as vDict

#setting up sleeper links
sApi="https://api.sleeper.app/v1/draft/"+str(boardNum)+"/picks"

#setting up youtube links
yt="https://www.youtube.com/watch?v="
yt2="&feature=emb_rel_err"
ytSearch="https://www.youtube.com/results?search_query="

#create player table
pTable=[]

#choiceActive set to false at the beginning so the first player loop doesn't play videos for the players already entered.
choiceActive=False

#initialize chromecast
if chromeCast:
    import pychromecast
    from pychromecast.controllers.youtube import YouTubeController
    chromecasts=pychromecast.get_chromecasts()
    chromecasts,browser=pychromecast.get_listed_chromecasts(friendly_names=[chromeCastName])
    try:
        cast=chromecasts[0]
        cast.wait()
        ytc=YouTubeController()
        cast.register_handler(ytc)
        print ("\n\nConnected to: "+chromeCastName+"!")
    except:
        print ("\n\n"+chromeCastName+" not found, vids will be displayed on this screen")
        chromeCast=False
else:
    # initialize selenium drivers and open draft boards
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    prefs={"profile.default_content_setting_values.notifications":2}
    youTubeOptions=webdriver.ChromeOptions()
    youTubeOptions.add_argument("--start-maximized")
    youTubeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
    youTubeOptions.add_experimental_option("prefs",prefs)
    youTubeDriver=webdriver.Chrome(options=youTubeOptions)
    youTubeDriver.get("https://www.youtube.com")
    
#this function plays the video found from youtube
def playVid(vLink):
    if chromeCast:
        ytc.play_video(vLink)
    else:
        youTubeDriver.get(yt+vLink+yt2)
        try:
            time.sleep(1)
            fullScreenButton=youTubeDriver.find_element(By.CLASS_NAME, 'ytp-fullscreen-button')
            fullScreenButton.click()
        except:
            print("Exception encountered attempting to play video in full screen")
    return 

#searches Youtube for link
def findVLink(fName,lName):
    try:
        url=ytSearch+fName+"+"+lName+"+highlights"
        response = requests.get(url)
        yhtml=response.text
        yhtml=yhtml[yhtml.find('href="/watch?v=')+15:]
        vLink=yhtml[:yhtml.find('"')]
        if "><" in vLink:
            yhtml=response.text
            yhtml=yhtml[yhtml.find('"videoId":"')+11:]
            vLink=yhtml[:yhtml.find('"')]
    except requests.exceptions.RequestException:
        vLink=""
    return vLink

#function runs when player is found on the draft board
def addPlayer(thisPlayer,pTable,choiceActive,vDict,vStr,fName,lName):
    if thisPlayer not in pTable:
        try:
            vLink=vDict[vStr]
        except KeyError:
            vLink=""
        if choiceActive:
            if vLink!="":
                playVid(vLink)
            elif autoSearch:
                vLink=findVLink(fName,lName)
                if vLink!="":
                    playVid(vLink)
        pTable.append(thisPlayer)
    return pTable

def skipAds():
    if chromeCast == False:
        try:
            skipE=youTubeDriver.find_element(By.CLASS_NAME, "ytp-ad-skip-button-container")
            skipE.click()
            time.sleep(1)
        except:
            nada=0
    return

while (True):
    skipAds()
    time.sleep(1) # 1 second wait in between api calls
    while True:
        try:
            response = requests.get(sApi)
            yJson=json.loads(response.text)
            break
        except requests.exceptions.RequestException:
            yJson=""
            print ("call to: "+sApi+" failed, trying again in 5 seconds")
            time.sleep(5)
    for x in range(0,len(yJson)):
        pos=yJson[x]["metadata"]["position"]+yJson[x]["metadata"]["team"]
        fName=yJson[x]["metadata"]["first_name"]
        lName=yJson[x]["metadata"]["last_name"]
        thisPlayer=[pos,fName,lName]
        vStr=pos+fName+lName
        pTable=addPlayer(thisPlayer,pTable,choiceActive,vDict,vStr,fName,lName)         
    choiceActive=True
    if len(pTable)>=(teams*rounds):
        break

if chromeCast==False:
    print("\n\nDraft completed! YouTube window will close in 5 minutes.\n\n")
    time.sleep(300)
    youTubeDriver.quit()