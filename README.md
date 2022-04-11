# web-scraping-challenge
Web Scraping Homework

This homework scrapes data and images from below websites:
1. https://redplanetscience.com/
2. https://galaxyfacts-mars.com/
3. https://spaceimages-mars.com/

The landing page has a button labelled "Get Data!". Please click on it to start scraping the data.
The scrapped data is pushed to MongoDB and the flask renders it back to our webpage.

The rendered page has featured image of MARS and latest news from https://redplanetscience.com/.
It also has facts from https://galaxyfacts-mars.com/ and the facts from this page are saved as mars_facts.html in "templates" folder.
The page also shows images of 4 Mars hemispheres scrapped from https://spaceimages-mars.com/ at the bottom of the page.
