import requests
import re
import string
import csv
import sys
import json
import os
import os.path
from bs4 import BeautifulSoup 
from collections import OrderedDict
from datetime import datetime
import re
# Global variable to store the list for JSON purposes
jsonList=[]

# HTMLParserBS class is used to find all URLs that reference to Social Media
class HTMLParserBS:    
    output_list=[]
    # method extractURLs is to extract all URLs and return them as the urls[] list
    # it goes through the website to find all anchors <a href>
    def extractURLs(self,page):      
        # all links are lowered because sometimes the same link is written differently, e.g., ug.edu.pl or UG.edu.pl
        soup = BeautifulSoup(page.text.lower(),"html.parser")
        urls = []
        for a in soup.find_all('a', href=True):
            urls.append(a['href'])
        return urls
    # method extractsURLs is to extract all URLs that are not in anchors <a>
    # it uses regular expression that search for any http or https, even not included in anchors
    def extractAllHTTP(self,page):
        URLs=re.findall(r"https?://[\w\-.~/?:#\[\]@!$&'()*+,;=]+", page.text.lower())
        return URLs

# class SocialMediaDeep contains a function responsible to divide the links into:
# (1) internal (used for the second search and external)
# (2) external (not used for the second search of social media)
class SocialMediaDeep:
    website=""    
    # this method is responsible to do the second search on subpages
    # from internal links that are present on the main page of the website
    def goDeeperToFindSocialMedia(self,website,URLs):
        print("Preparing to scrape subpages...")
        for url in URLs:
            try:        
                if url:
                    # the difference between InternalURL_type2 and InternalURL_type1
                    # is that type2 includes the domain name of the website, e.g., http://stat.gov.pl/page2.html
                    # and type1 does not include the domain name, e.g., <a href="./links/page2.html" ...>
                    if website in url and 'javascript' not in url:
                        print("Scraping InternalURL_type2: %s" % url)
                        smp.searchSocialMediaLinks(url,'2')
                    elif url[0]=="/" or url[0:1]=="./" or "http" not in url:
                        if url[0]=="/":
                            print("Scraping InternalURL_type1: {0} {1} ".format(website,url))
                            smp.searchSocialMediaLinks(website+url,'2')
                        elif url[0]==".":
                            print("Scraping InternalURL_type1: {0} {1}".format(website,url.replace('./','/')))
                            smp.searchSocialMediaLinks(website+url.replace('./','/'),'2')
                        else:
                            print("Scraping InternalURL_type1: {0} {1} {2}".format(website,'/',url))
                            smp.searchSocialMediaLinks(website+'/'+url,'2')
                    else:
                        # all external URLs are those who have a domain name different than the main page
                        print("ExternalURL_type1: %s " % url)                    
                else:
                    print("URL was not found in the second search.")
            except:
                print("Exception occured during processing the following URL:"+url)

class FileAccess:
    def jsonListWrite(self,jsonList): 
        currentDate = re.sub('[- :.]', '', str(datetime.now()))
        try:
            with open("wp2_social_"+currentDate+".json", "w") as file:
                file.write(str(jsonList))
                file.close()
        except IOError:
            msg = ("Error writing JSON file.")     
            print(msg)
            return

# class SocialMediaPresence includes one function responsible for finding popular Social Media websites
class SocialMediaPresence:
    website=""     
    # this method finds all social media links on webpage
    def searchSocialMediaLinks(self,website,level):        
        try:
            headers = {'user-agent': 'python-app/0.1 experimental for statistical purposes'}
            r = requests.get(website, headers=headers)            
        except:    
            print("Exception during scraping content of the webpage: "+website)
        else:
            print("The length of the scrapped content: %s characters" % str(len(r.text)))            
            rows=r.text.splitlines()
            # if facebook login button is present on the website - report this on the screen
            # not used now but maybe in the future it can enrich the ICT survey
            #for line in rows:
            #    if "facebookLoginButton" in line:
            #        print ("Facebook login found: %d" % line)
            p = HTMLParserBS()
            p.output_list=p.extractURLs(r)
            URLs=list(p.output_list)
            print("Number of links on website: %d" % len(URLs))
            # sets are used instead of lists to eliminate all duplicates automatically
            # sometimes inside the main page there are several links to Social Media, in this case all duplicates will be removed
            # but all Social Media links will be added to the final list
            facebook=set([]);
            twitter=set([]);
            linkedin=set([]);
            googleplus=set([]);
            instagram=set([]);
            youtube=set([]);
            none='';
            # modify this loop if you want to find more links
            for url in URLs:
                if url:
                    if "facebook.com" in url:
                        facebook.add(url)
                        print (url)
                    elif "twitter.com" in url:
                        twitter.add(url)
                        print (url)
                    elif "plus.google.com" in url:
                        googleplus.add(url)
                        print (url)
                    elif "linkedin.com" in url:
                        linkedin.add(url)
                        print (url)
                    elif "youtube.com" in url:
                        youtube.add(url)
                        print (url)
                    elif "youtu.be" in url:
                        youtube.add(url)
                        print (url)
                    elif "instagram.com" in url:
                        youtube.add(url)
                        print (url)
            if len(facebook)+len(twitter)+len(googleplus)+len(youtube)+len(instagram)+len(linkedin)==0:
                print('No social media links have been found.')
                none='1';
            else:
                print('Total number of unique social media links found: '
                      + str(len(facebook)+len(twitter)+len(googleplus)+len(youtube)+len(instagram)+len(linkedin)))
            # if subpage does not have a social media URL - do not write this in the result file
            if not (none=='1' and level=='2'):            
                try:
                    # name of the file
                    filename='wp2_social.csv'
                    exists=1
                    if not os.path.isfile(filename):
                        exists=0
                    with open (filename,'a') as file:
                        if exists==0: file.write("URL;Facebook;Twitter;Youtube;LinkedIn;Instagram;GooglePlus\n")
                        columnNames=['URL','Facebook','Twitter','Youtube','LinkedIn','Instagram','GooglePlus']                    
                        writer=csv.DictWriter(file,delimiter=';',dialect=csv.excel,fieldnames=columnNames)
                        writer.writerow({'URL':website,'Facebook':', '.join(facebook),'Twitter':', '.join(twitter),'Youtube':', '.join(youtube),'LinkedIn':', '.join(linkedin),'Instagram':', '.join(instagram),'GooglePlus':', '.join(googleplus)})
                except IOError:
                    msg = ("Error writing CSV file.")     
                    print(msg)      
                data={
                   'url' : website,
                   'Facebook' : list(facebook),
                   'Twitter' : list(twitter),
                   'Youtube' : list(youtube),
                   'LinkedIn' : list(linkedin),
                   'Instagram' : list(instagram),
                   'GooglePlus' : list(googleplus)
                }
                jsonList.append(data);
            smd=SocialMediaDeep();
            # if no links have been found on the main page, go one level deeper
            if none=='1' and level=='1' and len(URLs)>1:
                smd.goDeeperToFindSocialMedia(website,URLs)
  
smp=SocialMediaPresence()
fa=FileAccess()        
jsonList=[]
try:
    plik=open("url.txt","r")
except IOError:
    msg = ("Error reading URL file.\n\nPlease create a file named 'url.txt' in the current folder with the list of URLs you want to scrap.")
    msg += ("\n\nThe file content should be like this (one URL per line):\nmaslankowski.pl\nhttp://www.stat.gov.pl")
    print(msg)
else:
    for url in plik:
        if url!="":
            website='http://'+url.strip().replace('http://','').replace('https://','')
            print("Website currently being scrapped: "+website)
            smp.searchSocialMediaLinks(website,'1')
            print()
    fa.jsonListWrite(jsonList)
