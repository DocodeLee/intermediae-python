import requests
import xml.etree.ElementTree as ET

RSS_FEED_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml" 

def loadRss():
    "utility function to  load RSS feed"
    
    #HTTP request response
    response = requests.get(RSS_FEED_URL)
    
    return response.content
def parseXML(rss):
    """utility function to parse XML format rss feed
    """
    
    root = ET.fromstring(rss)
    newsitems = []
    for item in root.findall('./channel/item'):
        news = {}
        
        for child in item:
            
            if child.tag == "{http://search.yahoo.com/mrss/}content":
                news["media"] = child.attrib["url"]
            else:
                news[child.tag] = child.text.encode("utf8")
        newsitems.append(news)
    
    return newsitems
def topStories():
    rss = loadRss()
    newsitems = parseXML(rss)
    return newsitems