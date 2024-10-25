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

from flask import Flask, request

def bbscore():
  f=open("shasta.txt","r",encoding="utf-8")
  shasta = json.load(f)
  f.close()

  url=shasta["mbblink"]
  responce=urlopen(url)
  soup = BeautifulSoup(responce, features='html.parser')
  schoolName = soup.findAll("span",{"class": "long-name"})
  teamName = soup.findAll("span",{"class":"short-name"})

  homeScoreContainer = soup.findAll("div", {"class": "score icon-font-before"})
  awayScoreContainer = soup.findAll("div", {"class": "score icon-font-after"})
  
  cougar_score=homeScoreContainer[0].getText()
  enemy_score = awayScoreContainer[0].getText()

  if shasta["mbbhomegame"]=="no":
    temp = cougar_score
    cougar_score=enemy_score
    enemy_score=temp

  msg = schoolName[1].getText() + " " + cougar_score + " ------ " + enemy_score + " " + schoolName[0].getText()

  if cougar_score=="":
    msg = schoolName[1].getText() + " vs " + schoolName[0].getText() + " has not started yet!"
  return msg


def bbscoregetter():
  f=open("shasta.txt","r",encoding="utf-8")
  shasta = json.load(f)
  f.close()

  url=shasta["mbblink"]
  responce=urlopen(url)
  soup = BeautifulSoup(responce, features='html.parser')
  schoolName = soup.findAll("span",{"class": "long-name"})
  teamName = soup.findAll("span",{"class":"short-name"})

  homeScoreContainer = soup.findAll("div", {"class": "score icon-font-before"})
  awayScoreContainer = soup.findAll("div", {"class": "score icon-font-after"})
  
  cougar_score=homeScoreContainer[0].getText()
  enemy_score = awayScoreContainer[0].getText()

  if cougar_score=="":
    cougar_score=0
    enemy_score=0
  
  cougar_score=int(cougar_score)
  enemy_score=int(enemy_score)
  bbscore=cougar_score

  if shasta["mbbhomegame"]=="yes":
    temp = cougar_score
    cougar_score=enemy_score
    enemy_score=temp
    bbscore=cougar_score
  
  print(bbscore)
  
  bbtxtscore=shasta["mbbscore"]

  msg="SCORE IS TIED IF THIS SENDS THAT IS AN ISSUE"
  print("SAVED SCORE IS "+str(bbtxtscore))
  if(bbscore-1==bbtxtscore):
    msg="Free throw scored! Score is "+str(bbscore)
  elif(bbscore-2==bbtxtscore):
    msg="Coogs for two! Coogs now have "+str(bbscore)
  elif(bbscore-3==bbtxtscore):
    msg="Coogs for three! Coogs now have "+str(bbscore)
  elif(bbscore==bbtxtscore):
    msg="SCORE IS TIED IF THIS SENDS THAT IS AN ISSUE"
  else:
    msg = schoolName[1].getText() + " " + str(cougar_score) + " ------ " + str(enemy_score) + " " + schoolName[0].getText()
  print("okay what happened")

  shasta["mbbscore"]=bbscore
  f=open("shasta.txt","w",encoding="utf-8")
  json.dump(shasta,f,ensure_ascii=False)
  f.close()

  return msg






  #### WOMENS TEAM #####

def wbbscore():
  f=open("shasta.txt","r",encoding="utf-8")
  shasta = json.load(f)
  f.close()

  url=shasta["wbblink"]
  responce=urlopen(url)
  soup = BeautifulSoup(responce, features='html.parser')
  schoolName = soup.findAll("span",{"class": "long-name"})
  teamName = soup.findAll("span",{"class":"short-name"})

  homeScoreContainer = soup.findAll("div", {"class": "score icon-font-before"})
  awayScoreContainer = soup.findAll("div", {"class": "score icon-font-after"})
  
  cougar_score=homeScoreContainer[0].getText()
  enemy_score = awayScoreContainer[0].getText()

  if shasta["wbbhomegame"]=="no":
    temp = cougar_score
    cougar_score=enemy_score
    enemy_score=temp

  msg = schoolName[1].getText() + " " + cougar_score + " ------ " + enemy_score + " " + schoolName[0].getText()

  if cougar_score=="":
    msg = schoolName[1].getText() + " vs " + schoolName[0].getText() + " has not started yet!"
  return msg



  ############ FOOTBALL #############

def fbscoregetter():
  f=open("shasta.txt","r",encoding="utf-8")
  shasta = json.load(f)
  f.close()

  url=shasta["fblink"]
  responce=urlopen(url)
  soup = BeautifulSoup(responce, features='html.parser')
  schoolName = soup.findAll("span",{"class": "long-name"})
  teamName = soup.findAll("span",{"class":"short-name"})

  homeScoreContainer = soup.findAll("div", {"class": "score icon-font-before"})
  awayScoreContainer = soup.findAll("div", {"class": "score icon-font-after"})
  
  cougar_score=homeScoreContainer[0].getText()
  enemy_score = awayScoreContainer[0].getText()

  if cougar_score=="":
    cougar_score=0
    enemy_score=0
  
  cougar_score=int(cougar_score)
  enemy_score=int(enemy_score)
  bbscore=enemy_score

  if shasta["fbhomegame"]=="no":
    temp = cougar_score
    cougar_score=enemy_score
    enemy_score=temp
    bbscore=cougar_score
  
  print(bbscore,enemy_score)
  
  bbtxtscore=shasta["fbscore"]

  msg=bbtxtscore
  print("SAVED SCORE IS "+str(bbtxtscore))
  if(bbscore-7==bbtxtscore):
    msg="The kick is good! The Coogs have "+str(bbscore)
  elif(bbscore-6==bbtxtscore):
    msg="Extra point attempt is no good! Coogs now have "+str(bbscore)
  elif(bbscore-8==bbtxtscore):
    msg="The two point conversion is successful! Coogs now have "+str(bbscore)
  elif(bbscore-2==bbtxtscore):
    msg="SAFETY! The Coogs now have "+str(bbscore)
  elif(bbscore==bbtxtscore):
    msg="SCORE IS TIED IF THIS SENDS THAT IS AN ISSUE"
  else:
    msg = schoolName[1].getText() + " " + str(cougar_score) + " ------ " + str(enemy_score) + " " + schoolName[0].getText()
  print("okay what happened")

  shasta["fbscore"]=bbscore
  f=open("shasta.txt","w",encoding="utf-8")
  json.dump(shasta,f,ensure_ascii=False)
  f.close()

  return msg