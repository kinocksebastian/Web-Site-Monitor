# Web-Site-Monitor
Simple Python script to monitor updates on websties and tweet when update is happened. 

Introduction
------------
The files are :
1.siteComp.py - The main script
2.accessTokens - This File contains accessToken for twitter
3.consumerKeys - This File contains consumer token for Twitter
4.hashFile - This is the file used to store md5 hash of website
5.siteList.txt

How To Run
----------
Before Starting create an application in twitter and get consumerKeys. You can create application for twitter from https://apps.twitter.com/. After Getting consumer key and consumer secret key save in consumerKeys file. Then run twitterConfig.py file and follow the steps. twitterConfig file opens browser and asks for autharizing app by logging into twitter and given a pin after succesfully loggin in.  Enter the pin in twitterCOnfig.py and press enter. Now accessToken File will be generated. Keep the site name and url in siteList.txt. Now script is ready to run . 

python siteComp.py 
eg : python siteComp.py 

When it is run first time it generates hashFile which stores md5hash of webpage. This is used to find diffrence. For first execution script returns "Run for first time". From the second time onwards if there is any change it is updated to twitter account you authorised and if not it returns no update. 

Note : Dont FORGET to install TWEEPY package for python all other modules are in build in python. Keep all the files in same folder.
