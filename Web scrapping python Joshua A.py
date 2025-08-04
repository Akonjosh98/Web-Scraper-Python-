#!/usr/bin/env python
# coding: utf-8

# In[90]:


from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


# In[91]:


# First we need to send request from local pc to Amazon website and get HTML code so that we can get all other information.
# to view page code, click right click on page and click inspect, specifically to view title code, click on arrow at inspect area and click on title so it will navigate to that particular code where h2 header tag is present and class name to view text double on it, and to view page source u have to click right click on page and view page source which will redirect to html code page to get this we send request to the amazon page
# then copy the url which u want to scrap inside link= "",and to define HTTP header which is present before url at every website, whenever we visit any website on the internet you send http request to it, http request contains lot of things and one of them is header and inside the header you will find lot of different things and one of most important things is that user agent 
# User Agent tells that your trying to access this website and your genueine user by identifying your browser information and other information required to access the website


# In[92]:


URL = "https://www.amazon.in/s?k=boat+watches+for+men&i=electronics&crid=2T4ILOVGQM5EC&sprefix=boat+watc%2Celectronics%2C194&ref=nb_sb_ss_ts-doa-p_2_9"


# In[93]:


#Headers for request, we're defining header, inside {'User Agent':'paste ur own user agent here from what is my browser.com\myuseragent and we're also defining the language the accept language is en-US because inside the request we want to tell amazon that we want everything inEnglish language  '}
#Now we will be making requests to Amazon website,
HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0','Accept-Language': 'en-US, en;q=0.5'})


# In[94]:


#Now we will be making requests to Amazon website, to make request you will be using request package.get we will pass our url and we will pass our headers and run it
#HTTP Request
webpage = requests.get(URL, headers=HEADERS)


# In[95]:


webpage


# In[96]:


#To check the html content
webpage.content
#Currently this request is returning this html document into bytes format


# In[97]:


#To check what type, follow below type(webpage.content)
#As this is in byte format we need to properly convert it into proper HTML format, for that we will be using BeautifulSoup
type(webpage.content)


# In[98]:


# We use beautifulsoup function that we imported send (webcontent, and parse to 'html.parser' format)
# here bs=BeautifulSoup
soup = bs(webpage.content, 'html.parser')


# In[99]:


#here bytes converted to proper html document
soup


# In[100]:


#links = soup.find_all('a')


# In[101]:


#filtered_links = [link for link in links if 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal' in link.get('class', [])]


# In[102]:


# Now we're gonna scrap particular product link from amazon, 
# All of the links are written inside the 'a' tag its called as the anchor tags. to locate 'a'tag with product link, click on top left arrow symbol at inspect element, click on the product link it has to be in multiple products page to make the link active, and after clicking span and class will be visible above that you can see a tag with a link that's it.
# we can see <a class- "a-link-normal" is class info, and links are into 'href' element.
# Fetch links as list of Tag objects/ scraping product link from Amazon
#There's a function available inside the beautiful soup called find_all, find_all, finds all of the 'a' tags available inside our page that we extracted where the class name is whatever the class name that was inside 
#links = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})


# In[103]:


#data = soup.find_all('div',{'class':'a-row a-spacing-micro'})


# In[104]:


#print(data)


# In[105]:


#for link in soup.find_all('a'):
#print(link.get('href'))
#links=[]
#watch_name=[]
#start_link="https://www.amazon.in"


# In[131]:


links = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})


# In[132]:


links[1]


# In[133]:


# Now we will try to extract all of the link information, and after that we will loop through each and every link and build the proper function so that we will get everything automatically to extract one link all you have to do is..links(1), 1 because our product is sceond product in the multiple pages..
#links[1]



# In[134]:


# As you can see at above for a product link we are just getting half link over we need to append some things over here so here so first of all lets extract the link from and follow below steps
#links[1].get('href') # and your able to extract the actual link now
link = links[1].get('href') # Now we will store this in link variable


# In[135]:


#And for this we will append(attach/add) product link
product_link = "https://www.amazon.in" + link


# In[136]:


print(product_link)


# In[ ]:


# we're able to get the product link but not the right product link we called for link[1] but what we got is link[0], ok as it is first time in webscrapping
#Again we need to repeat the same process we need to make request to this

