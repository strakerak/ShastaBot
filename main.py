import os
import sys
import json
import re
import random
import time
import aiohttp
import urllib3
import random
from datetime import datetime
import pytz
from bs4 import BeautifulSoup
import requests

from urllib.parse import urlencode
from urllib.request import Request, urlopen

import scoregetter as sg
import commands as cmds

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)  #dont touch


@app.route('/', methods=['POST'])
def webhook():  #message analysis logic should go here
    data = request.get_json()
    log('Received {}'.format(data))
    print(data['group_id'])
    groups = [[]] #removed for anonymity
    groupid = data['group_id']
    botid = 'X'
    for i in range(0, len(groups)):
        if groups[i][0] == groupid:
            botid = groups[i][1]

    if data['name'] != "Shasta":  #not message from self


        f = open("shasta.txt", "r", encoding="utf-8")
        shasta = json.load(f)
        f.close()

        ###### THE FOLLOWING COMMANDS OR WORDS WILL GET RESPONSES FROM SHASTA #########
        if re.search('!pain', data['text'], re.IGNORECASE):
            msg = cmds.getpain()
            send_message(msg, groupid, botid)

        if "Rice" in data['text']:
            if randHund() > 95:
                msg = "Ruck Fice!"
                send_message(msg, groupid, botid)

        if re.search('new girl', data['text'], re.IGNORECASE):
            if randHund() > 90:
                msg = "Woah, you watch New Girl?"
                send_message(msg, groupid, botid)

        if re.search('reboot', data['text'], re.IGNORECASE) and re.search(
                'shasta', data['text'],
                re.IGNORECASE) and data['user_id'] != '36323537':
            msg = "You can't reboot me, only Boojangles can!"
            send_message(msg, groupid, botid)

        if re.search('reboot', data['text'], re.IGNORECASE) and re.search(
                'shasta', data['text'],
                re.IGNORECASE) and data['user_id'] == '36323537':
            msg = "You want me to reboot, okay!"
            send_message(msg, groupid, botid)
            msg = "Rebooting....."
            send_message(msg, groupid, botid)
            time.sleep(3)
            msg = "I am alive! Hello, I am Shasta!"
            send_message(msg, groupid, botid)

        if re.search('alma mater', data['text'], re.IGNORECASE):
            msg = cmds.getalma()
            #send_message(msg, groupid, botid)

        if re.search('!links', data['text'], re.IGNORECASE):
            msg = cmds.getlinks()
            send_message(msg, groupid, botid)

        if re.search('time', data['text'], re.IGNORECASE):
            print("Got the time")
            #msg = cmds.timegetter()
            #send_message(msg, groupid, botid)

        if re.search('Gort', data['text'], re.IGNORECASE):
            if randHund() > 89:
                msg = "ay gort sux lmao"
                send_message(msg, groupid, botid)

        if re.search('has left the group', data['text'],
                     re.IGNORECASE) and data['name'] == 'GroupMe':
            msg = "Doot Doot Doot. Another one bites the dust!"
            #send_message(msg, groupid, botid)
            #send_message("Press F to pay respects", groupid, botid)

        if re.search(' Baylor', data['text'], re.IGNORECASE):
            if randHund() > 95:
                msg = "Those bears are the worst, they aren't black bears. Bears. Beets. Battlestar Galactica!"
                send_message(msg, groupid, botid)

        if re.search('aggie', data['text'], re.IGNORECASE):
            if randHund() > 89:
                msg = "Sheep Fuckers"
                send_message(msg, groupid, botid)
        
        if re.search('use',data['text'],re.IGNORECASE):
          if randHund()>98:
            msg="Use me, I'm a dirty slut."
            #send_message(msg,groupid,botid)

        if re.search('A&M', data['text'], re.IGNORECASE):
            if randHund() > 89:
                msg = "Sheep Shaggers"
                send_message(msg, groupid, botid)

        if re.search('TAMU', data['text'], re.IGNORECASE):
            if randHund() > 89:
                msg = "Sheep Shaggers"
                send_message(msg, groupid, botid)

        if data['user_id'] == '43450137':
            if randHund() > 94:
                msg = "Alex is gay"
                send_message(msg, groupid, botid)
        if re.search(' UT', data['text'], re.IGNORECASE) or re.search(
                'University of Texas', data['text'], re.IGNORECASE):  #TAMU
            if randHund() > 95:
                msg = "HORNS DOWN!"
                send_message(msg, groupid, botid)
        
        if re.search('Shasta,',data['text'],re.IGNORECASE):
          msg = cmds.eball(data['text'])
          if msg!="DO NOT SEND":
            send_message(msg,groupid,botid)

        if re.search('removed', data['text'], re.IGNORECASE) and re.search(
                ' from the group.', data['text'], re.IGNORECASE):  #Try me
            msg = "I hope parking gives you a ticket"
            send_message(msg, groupid, botid)

        if re.search('added', data['text'], re.IGNORECASE) and re.search(
                ' to the group.', data['text'], re.IGNORECASE
        ) and data['name'] == 'GroupMe' and data['group_id'] == '47374201':
            msg = shasta["welcomemsg"]
            #send_message(msg, groupid, botid)

      
        '''if re.search(
                'joined', data['text'], re.IGNORECASE
        ) and data['name'] == 'GroupMe' and data['group_id'] == '47374201':
            msg = shasta["welcomemsg"]
            #send_message(msg, groupid, botid)'''

        if re.search('mask', data['text'], re.IGNORECASE):
            if randHund() > 47:
                msg = "Speaking of masks, you should wear one!"
                send_message(msg, groupid, botid)

        if re.search('whose house', data['text'], re.IGNORECASE):
            msg = "COOGS HOUSE!"
            send_message(msg, groupid, botid)

        if re.search(
                '!admin', data['text'],
                re.IGNORECASE) and data['group_id'] == '87997712' or re.search(
                    '!admin', data['text'],
                    re.IGNORECASE) and data['group_id'] == '61162957':
            msg = cmds.getadmin()
            send_message(msg, groupid, botid)

        ##### THIS SECTION HANDLES GETTING SCORES ######
        if re.search('shasta', data['text'], re.IGNORECASE) and re.search(
                'score', data['text'],
                re.IGNORECASE) or data['text'] == "!bbscore":
            msg = sg.bbscore()
            #send_message(msg, groupid, botid)

        if re.search('!fbscore', data['text'], re.IGNORECASE):
            msg = sg.fbscoregetter()
            #send_message(msg, groupid, botid)

        if re.search('!wbbscore', data['text'], re.IGNORECASE) or re.search(
                'women\'s basketball', data['text'], re.IGNORECASE):
            msg = ''
            #send_message(msg, groupid, botid)

        if shasta["mbbgameon"] == "yes":
            msg = sg.bbscoregetter()
            if msg != "SCORE IS TIED IF THIS SENDS THAT IS AN ISSUE":
                send_message(msg, groupid, botid)

        if shasta["fbgameon"] == "yes":
            msg = sg.fbscoregetter()
            if msg != "SCORE IS TIED IF THIS SENDS THAT IS AN ISSUE":
                send_message(msg, groupid, botid)

        if re.search(
                '!gamestatus', data['text'],
                re.IGNORECASE) and data['group_id'] == '87997712' or re.search(
                    '!admin', data['text'],
                    re.IGNORECASE) and data['group_id'] == '61162957':
            x = data['text']
            msg = cmds.gamestatus(x)
            send_message(msg, groupid, botid)

        if re.search(
                '!setgame', data['text'],
                re.IGNORECASE) and data['group_id'] == '87997712' or re.search(
                    '!admin', data['text'],
                    re.IGNORECASE) and data['group_id'] == '61162957':
            x = data['text']
            msg = cmds.setgame(x)
            send_message(msg, groupid, botid)

        if ((re.search(" has joined",data['text'],re.IGNORECASE)) and (data['group_id']=='61162957' or data['group_id']=='47374201')):
          josh = requests.get('https://api.groupme.com/v3/groups/groupinfo')
          joshload=json.loads(josh.text)
          #print(joshload)
          #print(joshload["response"]["members"])
          members = joshload["response"]["members"]

          msg = data['text']
          msg = msg[:-21]
          #print(msg)
          print("Finding memeber")
          for m in members:
            if msg==m["nickname"]:
              print("MATCH",msg,m["nickname"],m["name"],m["id"],m["user_id"])
              if data['name'] == "GroupMe" or data['name'] == "Shasta" or data['name']=="Mr. BooJangles":
                print("Sending DM to new member and adding to Group")
                send_dm(shasta["welcomemsg"], groupid, botid, m["user_id"], m)
                add_to_ann(groupid,botid,m["user_id"],m["nickname"])
                print("Done?")
              else:
                print("Should have worked but it ain't groupme")
            else:
              y=1
              #print(m["nickname"])
            

        ##### THIS HANDLES CHAT AND ANNOUNCEMENTS ####

        if (re.search('!chat', data['text'],
                     re.IGNORECASE) and data['group_id'] == '61162957') or (re.search('!chat', data['text'],
                     re.IGNORECASE) and data['group_id']=='87997712'): #First is self test, other is console
            #msg = cmds.chatter(data['text'])
            msg = data['text'][6:]
            print(msg)
            send_message(msg, '47374201', '5cb16ab7d4bac42824fc857acb')

        if (re.search('!alert', data['text'],
                     re.IGNORECASE) and data['group_id'] == '61162957') or (re.search('!alert', data['text'],
                     re.IGNORECASE) and data['group_id']=='87997712'): #First is self test, other is console
            #msg = cmds.chatter(data['text'])
            msg = data['text'][7:]
            print(msg)
            send_message(msg, 'removedForAnon', 'removedForAnon')

        if re.search('!announce', data['text'],
                     re.IGNORECASE) and data['group_id'] == '87997712' or (re.search('!announce',data['text'],re.IGNORECASE) and data['group_id']=='61162957'):
            jayz = data['text'].split()
            if jayz[0]=="!announce":
              member_ids=[]
              loci=[]
              josh = requests.get('https://api.groupme.com/v3/groups/groupinfo')
              joshload = json.loads(josh.text)
              members = joshload["response"]["members"]
              for m in members:
                member_ids.append((m["user_id"]))
                loci.append([0,6])
              #msg = cmds.announcer(data['text'])
              msg = "@coogs " + data['text'][10:]
              print(msg)
              announce_msg(msg, 'removdForAnon', 'removedForAnon',member_ids,loci)
        
        if re.search('!ban',data['text'],re.IGNORECASE):
          josh = requests.get('https://api.groupme.com/v3/groups/groupinfo') #47374201 this is cv3 announce
          joshload = json.loads(josh.text)
          members = joshload["response"]["members"]
          nickname2 = data['text']
          nickname=nickname2[5:]
          print(nickname)
          userID=0
          print(members[0])
          userNum=0
          for i in range(0,len(members)):
            if nickname==members[i]["nickname"]:
              userID=members[i]["id"]
              userNum=i
              break
          if ('admin' in members[userNum]['roles']) or ('owner' in members[userNum]['roles']):
            userID=0
            print("NO!")
          if userID!=0:
            requests.post('https://api.groupme.com/v3/groups/47374201/members/{}/remove?token='.format(userID))
          else:
            print("USER NOT FOUND")
          print(userID)

        if re.search(
                '!setwelcome', data['text'],
                re.IGNORECASE) and data['group_id'] == '87997712' or re.search(
                    '!admin', data['text'],
                    re.IGNORECASE) and data['group_id'] == '5189232':
            msg = cmds.setwelcome(data['text'])
            x = "Welcome message changed from: " + msg
            send_message(x, groupid, botid)
        
        if re.search('Happy Birthday',data['text'],re.IGNORECASE):
          if randHund()>89:
            msg = "https://youtu.be/cl3j7g390UY"
            send_message(msg,groupid,botid)

        if re.search('coogs suck lol',data['text'],re.IGNORECASE):
          #msg = "kik"
          print("kicking")
          #boosend(msg,groupid,botid,data['user_id'])
        
    return "ok", 200  #send all applicable messages


def randHund():
    int = random.randint(0, 101)
    return int


def getalert():
    url = 'http://alerts.uh.edu/'
    responce = urlopen(url)
    soup = BeautifulSoup(responce, features='html.parser')

    alertText = soup.findAll("div", {"class": "row"})
    print(alertText)
    msg = "https://www.youtube.com/watch?v=w5F_gfaX2B4?autoplay=1"
    return msg

def add_to_ann(g,botid,member_id,member_name):
  url='https://api.groupme.com/v3/groups/90461194/members/add?token='
  botid=str('removdForAnon')
  payload={"members":[]}
  guid = str(random.randint(0,100000))+str(random.randint(0,100000))+str(random.randint(0,100000))
  user = {"nickname":member_name,"user_id":member_id,"guid":guid}
  payload["members"].append(user)
  d=json.dumps(payload)
  print(d)
  response=requests.post(url,json=payload)
  print(response,response.text)


def send_dm(msg, g, botid, member_id, datas):
  url = 'https://api.groupme.com/v3/direct_messages?token='
  print(member_id,"A")
  botid=str('removedForAnon')
  direct_message = {
    "source_guid": str(random.randint(0,100000)) + str(random.randint(0,100000)) + str(random.randint(0,10000000)),
    "recipient_id": str(datas["user_id"]),
    "text" :msg
  }
  d=json.dumps(direct_message)
  print(d)
  payload={'direct_message': direct_message}
  response=requests.post(url,json=payload)
  print(response,response.text)

def announce_msg(msg, g, botid, member_ids,loci):
    from time import sleep
    sleep(0.1)
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id':
        str(botid),  #replace this code with above ones for corresponding GM
        'attachments':[{'loci': loci, 'type': 'mentions', 'user_ids': member_ids}],
        'text': msg
    }
    #request = Request(url, urlencode(data).encode())
    d = json.dumps(data)
    response = requests.post(url, data=d)


def send_message(msg, groupid, botid):
    from time import sleep
    sleep(0.1)
    url = 'https://api.groupme.com/v3/bots/post'


    data = {'bot_id':str(botid),'text': msg}
    #request = Request(url, urlencode(data).encode())
    #json = urlopen(request).read().decode()
    response = requests.post(url, params=data)


def boosend(msg, groupid, botid,memberid):
    from time import sleep
    sleep(0.1)
    url = 'https://api.groupme.com/v3/groups/{}/members/{}/remove?token='.format(groupid,memberid)


    data = {'token':'','text': msg}
    #request = Request(url, urlencode(data).encode())
    #json = urlopen(request).read().decode()
    response = requests.post(url, params=data)

def log(msg):
    print(str(msg))
    sys.stdout.flush()


def fbupdate_score():
    """Updates score from ESPN"""
    gameid = 401256140
    url = f'http://www.espn.com/college-football/game/_/gameId/' + str(gameid)
    responce = urlopen(url)
    soup = BeautifulSoup(responce, features='html.parser')

    schoolName = soup.findAll("span", {"class": "long-name"})
    teamName = soup.findAll("span", {"class": "short-name"})
    homeScoreContainer = soup.findAll("div",
                                      {"class": "score icon-font-before"})
    awayScoreContainer = soup.findAll("div",
                                      {"class": "score icon-font-after"})

    cougar_score = homeScoreContainer[0].getText()
    enemy_score = awayScoreContainer[0].getText()

    print(cougar_score, enemy_score)
    print(schoolName[0].getText())
    print(teamName)
    msg = schoolName[1].getText(
    ) + " " + cougar_score + " ------ " + enemy_score + " " + schoolName[
        0].getText()
    if cougar_score == "":
        msg = schoolName[1].getText() + " vs " + schoolName[0].getText(
        ) + " has not started yet!"
    return msg


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


