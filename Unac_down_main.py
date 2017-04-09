# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 16:36:17 2017

@author: Jeyaprabu J
"""
from bs4 import BeautifulSoup
from urllib import urlretrieve
import requests
import re
import os
import thread

def down_audio(img_link,lesson_name):
    code = re.search("https://player-images.unacademy.link/(.*)/images",img_link).group(1)
    aud_link = "https://player.unacademy.link/lesson-raw/"+code+"/audio."
#    print "\nDownloading Audio - "+lesson_name+" -",
    try:
        ret = urlretrieve(aud_link+"mp4",lesson_name+".mp4")  
        if (ret[1]["Content-Type"]) == "application/xml":
            ret = urlretrieve(aud_link+"mp3",lesson_name+".mp3")
        print "\nDownloaded ",lesson_name," -",(int(ret[1]["Content-Length"])/1024),"KB"
    except:
        print "Download Error"        
    
def down_slides(url,lesson_name,num=100):
    pos = len(url) if (url.find("?") is -1) else url.find("?")
    url = url[0:pos]
    u = re.search('(.*/).*\..*',url).group(1)
    ext = re.search('.*\.(.*)\?*.*',url).group(1)
    for i in range(2,num+1):
        link = u+str(i)+"."+ext
#        print "\nDownloading from %s" %link
        name = lesson_name+"_"+str(i)+"."+ext
        print "Downloading Slide : %s -" %name,
        try:
            ret = urlretrieve(link, name)
            if ret[1]["Content-Length"] == "0":
                os.remove(name)
                return
            print (int(ret[1]["Content-Length"])/1024),"KB"
        except:
            print "Download Error"

def image_link(lesson, lesson_number=1):
    r  = requests.get(lesson)
    data = r.text
    img_link = re.search(".*(https://player-images.unacademy.link/.*/images/.{8}).*",data).group(1)
    pos = img_link.find('"')
    img_link = img_link[0:pos]
    lesson_name = str(lesson_number) + "_" +re.search("\/lesson\/(.*)\/",lesson).group(1)
    if aud == "y":
        thread.start_new_thread(down_audio,(img_link,lesson_name))
    down_slides(img_link,lesson_name)

#link of first video of a lesson_name 
root = raw_input("Enter Unacademy URL: ")
lesson_name  = requests.get(root)
data = lesson_name.text
soup = BeautifulSoup(data)
lesson = list()
print "1. Whole lesson_name\n2. Particular Lesson"
choice = int(raw_input("Enter the Download Choice: "))
aud = raw_input("Need Audio? (y,n) :")
name = raw_input("Enter Name: ").replace(" ","_").replace(":","_")
try:
    os.mkdir(name)
    os.chdir(name)
except:
    print "Error While Creating Directory...Check for directory existence"
    exit

if choice == 1:
    #To find links for all lessons
    for link in soup.find_all('a'): 
        if ("/lesson/" in str(link.get('href'))) and ("/comment/" not in str(link.get('href'))):
            complete = "https://unacademy.com"+str(link.get('href'))
            if complete not in lesson:
                lesson.append(complete)
            #print link.get('href')
    #get link of all the slides  
    lesson_num = 0
    for i in lesson:
        lesson_num+=1
        image_link(i, lesson_num)
        
elif choice == 2:
    image_link(root)
    
