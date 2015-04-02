#!/usr/bin/python

import urllib2
import hashlib
import sys
import tweepy
from datetime import datetime,timedelta

#function to find change in website
def webSiteMonitor():
    with open("siteList.txt","r") as f:
        fileCounter = 1
        #give the user agent you like
        userAgent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
        for line in f:
            temp = line.replace(" ","")
            try:

                Message = line.split(',')[0]
                hashTags = line.split(',')[2]
                url = temp.split(",")[1]

            except:
                Message = line.split(',')[0]
                hashTags=""
                url = temp.split(",")[1]
                    
            fileName = Message + str(fileCounter) + "-Hash"
            try:
                hashFile = open(fileName,"r")
            except:
                #parsing website
                request = urllib2.Request(url)
                request.add_header('User-Agent',userAgent)
                opener = urllib2.build_opener()
                website = opener.open(request).read()

                #generating hash
                websiteHash = hashlib.md5(website).hexdigest()

                #writing to hash file
                hashFile = open(fileName,"w")
                hashFile.write(websiteHash)
                hashFile.close()
                print "Running The Script For First Time For " + Message
            
            else:
                #parsing website
                request = urllib2.Request(url)
                request.add_header('User-Agent',userAgent)
                opener = urllib2.build_opener()
                website = opener.open(request).read()

                #generating hash
                websiteHash = hashlib.md5(website).hexdigest()

                #reading old hash
                hashFile = open(fileName,"r")
                oldWebsiteHash = hashFile.readline().strip()
                hashFile.close()

                #writing new hash
                hashFile = open(fileName,"w")
                hashFile.write(websiteHash)
                hashFile.close()

                #comparing hash
                if(websiteHash != oldWebsiteHash):
                    print "Updating Twitter For update in " + Message
                    
                    #calling function to update twitter
                    updateTwitter(Message,hashTags)
                else:
                    print "No New Update For " + Message

        fileCounter = fileCounter + 1
        
def updateTwitter(Message,hashTags):
    #twitter auth procedures
    consumerKeyFile = open("consumerKeys","r")
    consumerKey = consumerKeyFile.readline().strip()
    consumerSecret = consumerKeyFile.readline().strip()
    consumerKeyFile.close()

    auth = tweepy.OAuthHandler(consumerKey,consumerSecret)
    accessTokenFile = open("accessTokens","r")
    accessToken = accessTokenFile.readline().strip()
    accessTokenSecret = accessTokenFile.readline().strip()
    accessTokenFile.close()

    auth.secure = True
    auth.set_access_token(accessToken,accessTokenSecret)
    api = tweepy.API(auth)

    #updating twitter
    updateTime = datetime.utcnow() - timedelta(hours=7)
    if(hashTags != ""):
        updateMessage = Message + " update detected at "  + updateTime.strftime("%Y-%m-%d %I:%M %p") + " PST " + hashTags
    else:
        updateMessage = Message + " update detected at "  + updateTime.strftime("%Y-%m-%d %I:%M %p") + " PST "
    api.update_status(status=updateMessage)
	
    
if __name__ == "__main__":
    
    #main function and calling diff
    webSiteMonitor() 
