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

from urllib.parse import urlencode
from urllib.request import Request, urlopen

def timegetter():
  schools = ["Rice","Texas A&M","Texas","SMU","Texas Tech","Texas State","UNT","UTEP","UTSA","Tulsa","Oklahoma","OU","Tulane"]
  t = pytz.timezone("America/Chicago")
  ht=datetime.now(t)
  ct=ht.strftime("%H:%M")
  msg = "The time is " + ct + " and " + random.choice(schools) + " still sucks!"
  return msg

def getalma():
  msg="All hail to thee,\nOur Houston University.\nOur hearts fill with gladness\nWhen we think of thee.\nWe'll always adore thee\nDear old varsity\nAnd to they memory cherised,\nTrue we'll ever be."
  return msg

def getpain():
  msg ="https://i.groupme.com/960x639.jpeg.a607644da2bd4787a626f672d4be5b00.large"
  return msg


def eball(x):
  eballs=["As I see it, yes!","Ask again later","Better not tell you now.","Cannot predict now","Concentrate and ask again","Don't count on it","It is certain.","Most likely","My reply is no","My sources say no","Outlook not so good","Outlook good","Reply hazy, try again","Signs point to yes","Very doubtful","Without a doubt","Yes.","Yes, - definitely","You may rely on it"]
  spl=x.split()
  j=spl[-1]
  if spl[0]=="Shasta," or spl[0]=="shasta," and j[-1]=="?":
    msg = random.choice(eballs)
  else:
    msg = "DO NOT SEND"
  return msg

def gamestatus(x):
  f = open("shasta.txt","r",encoding="utf-8")
  shasta = json.load(f)
  f.close()
  args = x.split()
  if len(args)!=3:
    return "Format: !gamestatus {bb/wbb/fb} {on/off}"
  if args[1]=="bb":
    print("basketball")
    if args[2]=="off":
      shasta["mbbgameon"]="no"
    elif args[2]=="on":
      shasta["mbbgameon"]="yes"
    else:
      return "Error"
  elif args[1]=="wbb":
    if args[2]=="off":
      shasta["wbbgameon"]="no"
    elif args[2]=="on":
      shasta["wbbgameon"]="yes"
    else:
      return "Error"
  elif args[1]=="fb":
    if args[2]=="off":
      shasta["fbgameon"]="no"
    elif args[2]=="on":
      shasta["fbgameon"]="yes"
    else:
      return "Error"
  else:
    return "Error"
  
  try:
    f=open("shasta.txt","w",encoding="utf-8")
    json.dump(shasta,f,ensure_ascii=False)
    f.close()
  except:
    return "Error updating"

  return "Game Status updated successfully"

  
def setgame(x):
  f = open("shasta.txt","r",encoding="utf-8")
  shasta = json.load(f)
  f.close()
  args = x.split()
  print(len(args))
  if len(args)!=5:
    return "Format: !setgame {wbb/bb/fb} {on/off} {supporting ESPN link} {yes/no} <-- if the game is at home"
  if args[1]=="bb":
    print("basketball")
    if args[2]=="off":
      shasta["mbbgameon"]="no"
    elif args[2]=="on":
      shasta["mbbgameon"]="yes"
    else:
      return "Error"
    try:
      f=open("shasta.txt","w",encoding="utf-8")
      json.dump(shasta,f,ensure_ascii=False)
      f.close()
    except:
      return "Error updating"
    
    shasta["mbblink"]=args[3]
    if args[4]=="yes":
      shasta["mbbhomegame"]="yes"
    elif args[4]=="no":
      shasta["mbbhomegame"]="no"
    else:
      return "Error for home game input"
  elif args[1]=="wbb":
    if args[2]=="off":
      shasta["wbbgameon"]="no"
    elif args[2]=="on":
      shasta["wbbgameon"]="yes"
    else:
      return "Error"
    try:
      f=open("shasta.txt","w",encoding="utf-8")
      json.dump(shasta,f,ensure_ascii=False)
      f.close()
    except:
      return "Error updating"

    shasta["wbblink"]=args[3]
    if args[4]=="yes":
      shasta["wbbhomegame"]="yes"
    elif args[4]=="no":
      shasta["wbbhomegame"]="no"
    else:
      return "Error for home game input"
    
  elif args[1]=="fb":
    if args[2]=="off":
      shasta["fbgameon"]="no"
    elif args[2]=="on":
      shasta["fbgameon"]="yes"
    else:
      return "Error"
    try:
      f=open("shasta.txt","w",encoding="utf-8")
      json.dump(shasta,f,ensure_ascii=False)
      f.close()
    except:
      return "Error updating"

    shasta["fblink"]=args[3]
    if args[4]=="yes":
      shasta["fbhomegame"]="yes"
    elif args[4]=="no":
      shasta["fbhomegame"]="no"
    else:
      return "Error for home game input"
  else:
    return "Error"
  
  try:
    f=open("shasta.txt","w",encoding="utf-8")
    json.dump(shasta,f,ensure_ascii=False)
    f.close()
  except:
    return "Error updating"

  return "Game Status updated successfully"



def chatter(x):
  wrds=[]
  strn=x
  spl=strn.split()
  wrds=spl[1:]
  strn=""
  for w in wrds:
    strn=strn+" "+w
  msg = strn
  return msg

def announcer(x):
  wrds=[]
  strn=x
  spl=strn.split()
  wrds=spl[1:]
  strn="@coogs"
  for w in wrds:
    strn=strn+" "+w
  msg = strn
  return msg

def setwelcome(x):
  #wrds=[]
  #strn=x
  #spl=strn.split()
  #wrds=spl[1:]
  strn=x[12:]
  
  f=open("shasta.txt","r",encoding="utf-8")
  shasta = json.load(f)
  f.close()

  msg=shasta["welcomemsg"]
  shasta["welcomemsg"]=strn

  try:
    f=open("shasta.txt","w",encoding="utf-8")
    json.dump(shasta,f,ensure_ascii=False)
    f.close()
  except:
    return msg
  
  return msg

def getlinks():
  msg = "Discord: https://discord.gg/t5Sr3yh\nClub Merch (PM Mr. BooJangles to get): https://imgur.com/a/mQZaa8m\nInsta/Twitter: coogsofcv3\nMinecraft IP Address: mc.thequad.dev\nUH Achievements: https://sites.google.com/view/uhachievements"
  return msg

def getadmin():
  msg = "ADMINS: If a command is incomplete, type it out to get the format\n\n!setgame -> Allows admins to set the game for wbb, bb, or fb.\n\n!gamestatus -> Allows you to toggle automatic updates for games on/off for wbb, bb, or fb\n\n !setwelcome -> Just type the welcome message after this. It will automatically update. Be very careful with this."
  return msg

def getswear(x):
  swears=["Cauldron Bum!","Son of a Banshee!","Swish and Flicker!","VOLDEMORT'S NIPPLE!","DRAGON BOGIES!","EXPECTO PATRONADS!!","Jiggery Pokery ^-^","Blast-Ended Skank!","YOU'RE SUCH A BROOM HEAD!","Hagrid's... Buttkwak", "LEPRECHAUN TAINT!","Unicorn Turds!","MUGGLE FUCKING TROLL SHIT", "You Floppy-Wanded Dementor Boggerer","DOBBYS SOCK!","Flapdoodle!"]
  swear = random.choice(swears)
  if swear == "MUGGLE FUCKING TROLL SHIT":
    msg = swear + " " + x.upper()
    return msg
  else:
    msg = swear
    return msg