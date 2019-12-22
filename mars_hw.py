#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
from bs4 import BeautifulSoup
import urllib.request
import time
import pandas as pd


# In[2]:


# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# In[3]:


# Define database and collection
db = client.nasa_db
collection = db.articles


# In[4]:


#https://splinter.readthedocs.io/en/latest/drivers/chrome.html
get_ipython().system('which chromedriver')


# In[5]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[6]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[7]:


html = browser.html
soup = BeautifulSoup(html, "html.parser")
    


# In[ ]:





# In[8]:


results = soup.find_all('body')
results


# In[9]:


#document.querySelector("#page > div.grid_list_page.module.content_page > div > article > div > 
#section > div > ul > li:nth-child(1) > div > div > div.content_title > a")

#document.querySelector("#page > div.grid_list_page.module.content_page > div > article > div > section > div > ul >
#li:nth-child(1) > div > div > div.article_teaser_body")


# In[10]:


for result in results:
    # scrape the article header 
    news_title = result.find('div', class_='content_title').text
    news_p = result.find('div', class_='article_teaser_body').text
    
    
print (news_title)
print (news_p)


# In[11]:


new_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(new_url)


# In[12]:


#<img src="/spaceimages/images/mediumsize/PIA17845_ip.jpg" class="fancybox-image" style="display: inline;">
# https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA17845_ip.jpg

#  <div class="fancybox-inner fancybox-skin fancybox-dark-skin fancybox-dark-skin-open" style="border-width: 
#10px; margin-top: -10px; margin-left: -10px; overflow: visible; width: 515px; height: 382px;"><img src="/s
#paceimages/images/mediumsize/PIA17845_ip.jpg" class="fancybox-image" style="display: i
#nline;"><a title="Previous" class="fancybox-nav fancybox-prev" href="javascript:;"><span></span></a><a ti
#tle="Next" class="fancybox-nav fancybox-next" href="javascript:;"><span></span></a><a title="Expand image" 
#class="fancybox-expand" href="javascript:;" style="display: none;"></a></div>



#<a class="button fancybox" data-description="Hurricane Dorian off the coast 
#of Florida, as seen by the small satellite TEMPEST-D at 2 a.m. EDT on Sep. 3, 2019 
#(11 p.m PDT on Sept. 2, 2019). The layers in the animation reveal slices of the hurricane from four depths."
#data-fancybox-group="images" data-fancybox-href="/spaceimages/images/mediumsize/PIA23431_ip.jpg" 
#data-link="/spaceimages/details.php?id=PIA23431" data-title="TEMPEST-D CubeSat Sees Hurricane Dorian in 3D" id="full_image">
#					FULL IMAGE
#				  </a>


# In[13]:


html_2 = browser.html
soup = BeautifulSoup(html_2, "html.parser")


# In[14]:


results_2 = soup.find_all('body')
#results_2
results_2


# In[15]:


for res in results_2:
    img_url = res.find_all('a', class_='button fancybox')
#
img_url
    


# In[16]:


for res in results_2:
    img_url = res.find('a', class_='button fancybox')['data-fancybox-href']
#
img_url
    


# In[17]:


x = (new_url.split ("spaceimages/?search=&category=Mars"))[0]
x


# In[18]:


whos


# In[19]:


actual_url = x + img_url
print(actual_url)
browser.visit(actual_url)


# In[20]:


mars_weather_url = "https://twitter.com/marswxreport?lang=en"
browser.visit(mars_weather_url)


# In[21]:


html_3 = browser.html
soup = BeautifulSoup(html_3, "html.parser")


# In[22]:


results_3 = soup.find_all('body')
#results_2
results_3


# In[23]:


#<p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" lang="en" data-aria-label-part="0">InSight sol 377 (2019-12-18) low -97.5ºC (-143.6ºF) high -19.9ºC (-3.9ºF)
#winds from the SSE at 6.4 m/s (14.3 mph) gusting to 21.0 m/s (47.1 mph)
#pressure at 6.50 hPa<a href="https://t.co/hPiRp43HDU" class="twitter-timeline-link u-hidden" data-pre-embedded="true" dir="ltr">pic.twitter.com/hPiRp43HDU</a></p>


for r in results_3:
    tweet = r.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
#
tweet
    


# In[24]:


splitted = tweet.split("\n")
splitted 


# In[25]:


split2 = splitted [2].split("pic.twitter.com/")
split2


# In[26]:


split2 [0]


# In[27]:


weather_tweet = splitted [0] + " " + splitted [1] + " " +  split2 [0]


# In[28]:


weather_tweet


# In[29]:


facts_url = "https://space-facts.com/mars/"
browser.visit(facts_url)


# In[30]:


tables = pd.read_html(facts_url)
tables


# In[31]:


html_1 = tables [0].to_html()
tables [0].to_html("mars.html")


# In[32]:


html_2 = tables [1].to_html()
tables [1].to_html("mars2.html")


# In[33]:


hempispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hempispheres_url)


# In[35]:


html_4 = browser.html
h_soup = BeautifulSoup(html_4, "html.parser")
  


# In[119]:


#results_4 = h_soup.find_all('a', class_= 'itemLink product-item')
#results_4
#for resu in results_4:
    #hem = resu.find_all('a', class_= 'itemLink product-item')
#hem

new_list = []
for ana in h_soup.findAll('a', class_= 'itemLink product-item'):
  if ana.parent.name == 'div':
    new_list.append(ana["href"])
    
evens = new_list[1::2]
evens


# In[120]:


h_urls = []
new_url = hempispheres_url.split("/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")[0]
for eve in evens:
    h_urls.append (new_url + eve)
h_urls


    


# In[162]:


images = []
titles = []
for hur in h_urls:
    browser.visit(hur)
    html_5 = browser.html
    h_soup = BeautifulSoup(html_5, "html.parser")
    picture_link = h_soup.find('a',href=True,text="Sample").get('href')
    title = h_soup.find("h2", class_="title").get_text()
    title = title.split("Enhanced")[0]
    images.append(picture_link)
    titles.append(title)
for image in images: 
    browser.visit(image)
    


# In[133]:


#<a target="_blank" 
#href="http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg">Sample</a>
results_5


# In[129]:





# In[ ]:




