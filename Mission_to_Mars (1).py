#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup as bs
import os
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pymongo


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


news_url = 'https://redplanetscience.com/'
browser.visit(news_url)


# In[8]:


news_html = browser.html
soup = bs(news_html, 'html.parser')


# In[9]:


#News Title
news_title = soup.find('div', class_='content_title').text
print(news_title)


# In[10]:


#News Paragraph
news_p = soup.find('div', class_='article_teaser_body').text
print(news_p)


# In[315]:


#Photo
url='https://spaceimages-mars.com'
browser.visit(url)


# In[316]:


browser.links.find_by_partial_text("FULL IMAGE").click()


# In[326]:


pic_html = browser.html
soup = bs(pic_html,'html.parser')
pic_html = "/image/featured/mars"
print(url)
print(pic_html)


# In[327]:


featured_image_url = url + pic_html
featured_image_url


# In[254]:


#Facts
facts_url = 'https://galaxyfacts-mars.com'
browser.visit(facts_url)


# In[255]:


facts_html = browser.html
soup = bs(facts_html, 'html.parser')
#mars_facts = soup.find('table', class_ = 'tbody')


# In[256]:


mars_table = pd.read_html(facts_html)
mars_table


# In[257]:


mars_df = mars_table[0]
mars_df


# In[258]:


mars_df.columns = ["Categories", "Mars", "Earth"]
mars_df


# In[264]:


marshtml = (mars_df.to_html())


# In[265]:


print(marshtml)


# In[267]:


mars_df.to_csv('../marsData.csv',index=False)


# In[260]:


#Hemisphere
hemi_url = "https://marshemispheres.com/"
browser.visit(hemi_url)


# In[261]:


hemi_html = browser.html
soup = bs(hemi_html, "html.parser")


# In[262]:


hemi = soup.find_all("div", class_="item")
#hemi


# In[279]:


hemi_info = []
for result in hemi:
    h_title = result.find("h3").text
    hemi_img = x.find("a", class_="itemLink product-item")["href"]
    
    browser.visit(hemi_url + hemi_img)
    
    image_html = browser.html
    web_info = bs(image_html, "html.parser")
    
    #browser.links.find_by_partial_text('Next').click()
    try:
        
        img_url = hemi_url + web_info.find("img", class_="wide-image").link
        browser.links.find_by_partial_text('Next').click()
    except:
        ""
    
    hemi_info.append({"title":h_title, "img_url":img_url})
    
    print(h_title)
    print(img_url)


# In[ ]:




