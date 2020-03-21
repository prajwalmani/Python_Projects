import requests # pip install requests
import xml.etree.ElementTree as et

# You can add any rss feed url based on your liking
rss_feed_url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

def loadrss():
    # to get the https info
    resp = requests.get(rss_feed_url)
    return resp.content
def parseXML(rss):
    # function to parse the xml
    root = et.fromstring(rss)
    # create a empty list
    newslist = []
    for item in root.findall('./channel/item'):
        news = {}
        for child in item:
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media']=child.attrib['url']
            else:
                news[child.tag]=child.text.encode("utf8")
        newslist.append(news)
    return newslist
def topstories():
    rss = loadrss()
    newslist =  parseXML(rss)
    return newslist


