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
from threading import Thread

t = list()

def down_audio(img_link, lesson_name):
    code = re.search("https://player-images.unacademy.link/(.*)/images", img_link).group(1)
    aud_link = "https://player.unacademy.link/lesson-raw/" + code + "/audio."
#    print "\nDownloading Audio - "+lesson_name+" -",
    try:
        ret = urlretrieve(aud_link+"mp4", lesson_name+".mp4")  
        if (ret[1]["Content-Type"]) == "application/xml":
            ret = urlretrieve(aud_link+"mp3", lesson_name+".mp3")
        print "\nDownloaded Audio ", lesson_name, " -", (int(ret[1]["Content-Length"])/1024), "KB"
    except:
        print "Download Error"        
    
def down_slides(url, lesson_name, num=100):
    pos = len(url) if (url.find("?") is -1) else url.find("?")
    url = url[0:pos]
    u = re.search('(.*/).*\..*', url).group(1)
    ext = re.search('.*\.(.*)\?*.*', url).group(1)
    for i in range(2, num+1):
        link = u + str(i) + "." + ext
#        print "\nDownloading from %s" %link
        name = lesson_name + "_" + str(i) + "." + ext
        print "Downloading Slide : %s -" %name,
        try:
            ret = urlretrieve(link, name)
            if ret[1]["Content-Length"] == "0":
                os.remove(name)
                print "Not Available"
                return
            print (int(ret[1]["Content-Length"])/1024),"KB"
        except:
            print "Download Error"

def image_link(lesson, aud, lesson_number=1):
    r  = requests.get(lesson)
    data = r.text
    img_link = re.search(".*(https://player-images.unacademy.link/.*/images/.{8}).*", data).group(1)
    pos = img_link.find('"')
    img_link = img_link[0:pos]
    lesson_name = str(lesson_number) + "_" + re.search("\/lesson\/(.*)\/", lesson).group(1)
    if aud == "y":
        s = Thread(target = down_audio, args = (img_link, lesson_name))
        t.append(s)
        s.start()
    down_slides(img_link, lesson_name)

def start_download():
    #link of first video of a lesson_name 
    root = raw_input("Enter Unacademy URL: ")
    try:
        lesson_name  = requests.get(root)
    except:
        print "Enter Valid Unacademy URL"
        return
    data = lesson_name.text
    soup = BeautifulSoup(data)
    lesson = list()
    print "1. Whole lesson_name\n2. Particular Lesson"
    choice = int(raw_input("Enter the Download Choice: "))
    aud = raw_input("Need Audio? (y,n) :")
    while 1:
        try:
            name = raw_input("Enter Name: ").replace(" ","_").replace(":","_")
            cwd = os.getcwd()
            os.mkdir(name)
            os.chdir(name)
            break
        except:
            print "Error While Creating Directory...Check if directory already Exist"
            continue
    
    if choice == 1:
        #To find links for all lessons
        for link in soup.find_all('a'): 
            if ("/lesson/" in str(link.get('href'))) and ("/comment/" not in str(link.get('href'))):
                complete = "https://unacademy.com"+str(link.get('href'))
                if complete not in lesson:
                    lesson.append(complete)
        #get link of all the slides  
        lesson_num = 0
        for i in lesson:
            lesson_num+=1
            image_link(i, aud, lesson_num)
            
    elif choice == 2:
        image_link(root, aud)
    
    print "Waiting for All Downloads to Complete"
    for i in t:
        i.join()
    print "Downloads Completed"
    os.chdir(cwd)

print "Welcome to Unacademy Downloader"
while 1:
    start_download()
    print "1. Download Another Course\n2. Exit"
    choice = raw_input("Enter your Choice :")
    if choice == "1":
        continue
    else:
        break
