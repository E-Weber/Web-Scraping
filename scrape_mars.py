import pandas as pd
from bs4 import BeautifulSoup as bs
import os
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from flask_PyMongo import PyMongo
from flask import Flask, render_template
import time


def init_browser():

    #browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


def scrape():

    data = {}

    news_url = 'https://redplanetscience.com/'
    browser.visit(news_url)
    time.sleep(2)

    # Parser
    news_html = browser.html
    soup = bs(news_html, 'html.parser')

    # News Title
    data['news_title'] = soup.find('div', class_='content_title').get_text

    # News Paragraph
    data['news_p'] = soup.find('div', class_='article_teaser_body').get_text

    # Photo
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # click
    browser.links.find_by_partial_text("FULL IMAGE").click()

    # Findimage
    pic_html = browser.html
    soup = bs(pic_html, 'html.parser')
    pic_html = "/image/featured/mars"

    # Featured url
    featured_image_url = url + pic_html
    data['featured_image_url'] = featured_image_url

    # Facts
    facts_url = 'https://galaxyfacts-mars.com'
    browser.visit(facts_url)

    # Parser
    facts_html = browser.html
    soup = bs(facts_html, 'html.parser')

    # Table
    mars_table = pd.read_html(facts_html)
    mars_table

    # MarsDF
    mars_df = mars_table[0]
    mars_df

    # Add Columns
    mars_df.columns = ["Categories", "Mars", "Earth"]
    mars_df

    # Convert DF to html
    print(mars_df.to_html())

    # Export to CSV
    mars_df.to_csv('../marsData.csv', index=False)

    # Hemisphere
    hemi_url = "https://marshemispheres.com/"
    browser.visit(hemi_url)

    # Parser
    hemi_html = browser.html
    soup = bs(hemi_html, "html.parser")

    # Find all class_ "items"
    hemi = soup.find_all("div", class_="item")
    hemi

    # Appendlist
    hemi_info = []

    # for loop
    for result in hemi:
        h_title = result.find("h3").text
        hemi_img = x.find("a", class_="itemLink product-item")["href"]

        browser.visit(hemi_url + hemi_img)

        image_html = browser.html
        web_info = bs(image_html, "html.parser")
        img_url = hemi_url + web_info.find("img", class_="wide-image")["src"]

        try:
            browser.links.find_by_partial_text('next').click

        except:
            ""

        hemi_info.append({"title": h_title, "img_url": img_url})

    browser.quit
    return data


print(scrape())
