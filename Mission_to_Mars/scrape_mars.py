from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():



    # In[2]:


    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


# Code to scrape news related to Mars

# In[3]:


    url = 'https://redplanetscience.com/'
    browser.visit(url)


# In[4]:


    for x in range(1):
    
        n_title = []
        n_desc = []

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        articles = soup.find_all(class_='list_text')
        print(type(articles))

        for article in articles:
            news_title = article.find(class_='content_title').text
            news_p = article.find(class_='article_teaser_body').text
            n_title.append(news_title)
            n_desc.append(news_p)
        try:
            lat_title = n_title[0]
            lat_art = n_desc[0]
          
        except:
            print(n_title)

    
#latest_news = pd.DataFrame({"Title": lat_title, "Article": lat_art})
#latest_news

    #print(lat_title)
   # print(lat_art)

        
        
# Click the 'Next' button on each page
 #    try:

  #       browser.links.find_by_partial_text('MORE').click()
  #   except:
   #      print("Scraping Complete")


# Code to scrape image in headline

# In[8]:


    url2 = 'https://spaceimages-mars.com/'
    browser.visit(url2)


# In[9]:


    browser.links.find_by_partial_text('FULL IMAGE').click()


# In[12]:




    html2 = browser.html
    soup2 = BeautifulSoup(html2, 'html.parser')
    images = soup2.find_all('div', class_='fancybox-outer')


    for image in images:
        path = image.find('img', class_= 'fancybox-image')
        relative_image_path = path['src']
        mars_img = url2 + relative_image_path
        print (mars_img)
        


# Code to scrape facts about Mars

# In[3]:


    url3 = 'https://galaxyfacts-mars.com/'
    browser.visit(url3)


# In[4]:


    tables = pd.read_html(url3)


# In[5]:


    tables


# In[6]:


    type(tables)


# In[18]:


#keep first object in the list and drop the rest
    df = tables[0]
    df.columns = df.columns.get_level_values(0)
    df.head()


# In[19]:


#Replace column header with first row
    df.columns = df.iloc[0]
    df = df[1:]
#Delete Earth column and replace column headers
    df = df.drop(['Earth'], axis=1)
    df.rename(columns={'Mars - Earth Comparison': 'Description', 'Mars': 'Facts'}, inplace=True)
    df.head()


# In[20]:


#convert to html and save the html file
    html_table = df.to_html()
    html_table.replace('\n', '')
    df.to_html('templates/mars_facts.html')


# More pictures from different hemispheres

# In[43]:


    url4 = 'https://marshemispheres.com/'
    browser.visit(url4)
    hemispheres = ["Cerberus Hemisphere", "Schiaparelli Hemisphere", "Syrtis Major Hemisphere", 
               "Valles Marineris Hemisphere"]
    img_url = []


    dict = {}


    for i in range(len(hemispheres)):
    
        browser.links.find_by_partial_text(hemispheres[i]).click()
    
        html3 = browser.html
        soup3 = BeautifulSoup(html3, 'html.parser')
        images = soup3.find_all('div', class_='wide-image-wrapper')


        for image in images:
            path2 = image.find('img', class_= 'wide-image')
            relative_image_path2 = path2['src']
            img2 = url4 + relative_image_path2
            img_url.append(img2)
    
    
    
        browser.links.find_by_partial_text('Back').click()
    
    for j in range(len(hemispheres)):
        dict[hemispheres[j]] = img_url[j]
                
    print(dict)
                


    all_mars_data = {
        "main_title": lat_title,
        "main_art": lat_art,
        "main_img": mars_img,
        "mars_hem": dict
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return all_mars_data
{}
    
