import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    LOGIN_LINK,
    EMAIL_INPUT,
    CONTINUE_EMAIL,
    PASSWORD_INPUT,
    LOGIN_BUTTON,
    SCROLL_TO_TECH_HEADER_LINK,
    TOP_ACCOUNT_BUTTON,
    ACCOUNT_LINK,
    ACCOUNT_ACC_NO,
    ACCOUNT_EMAIL,
)


URL = 'https://www.nytimes.com/'
TECH_HEADER_URL = 'https://www.nytimes.com/section/technology'

USERNAME = ''
PASSWORD = ''


driver = webdriver.Chrome(executable_path='chromedriver')
driver.maximize_window()
wait = WebDriverWait(driver, 120)


def login():
    driver.get(URL)
    driver.find_element(*LOGIN_LINK).click()
    wait.until(EC.presence_of_element_located(EMAIL_INPUT)).click()

    driver.find_element(*EMAIL_INPUT).send_keys(USERNAME)
    driver.find_element(*CONTINUE_EMAIL).click()
    wait.until(EC.presence_of_element_located(PASSWORD_INPUT)).click()
    driver.find_element(*PASSWORD_INPUT).send_keys(PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()
    wait.until(EC.visibility_of_element_located(TOP_ACCOUNT_BUTTON))


def scrap_articles():
    # go to tech page
    driver.get(TECH_HEADER_URL)
    wait.until(EC.element_to_be_clickable(SCROLL_TO_TECH_HEADER_LINK))
    latest_tech_section = driver.find_element(*SCROLL_TO_TECH_HEADER_LINK)
    # scroll down to latest section
    latest_tech_section.send_keys(Keys.PAGE_DOWN)

    soup = BeautifulSoup(driver.page_source, features="html.parser")

    latest_article_div = soup.find(id='stream-panel')
    articles = []
    olist = latest_article_div.find('ol')
    # extract acticles info
    for article in olist.find_all('li'):
        title = article.find('h2').get_text()
        author = article.find("span", {"class": "css-1n7hynb"}).get_text()
        summary = article.find('p').get_text()
        published_date = article.find('span', {'data-testid': "todays-date"}).get_text()
        articles.append({
            'title': title,
            'author': author,
            'summary': summary,
            'published_date': published_date,
        })

    with open('articles.json', 'w') as file:
        json.dump(articles, file)


def scrap_account_info():
    account_btn = driver.find_element(*TOP_ACCOUNT_BUTTON)
    # scroll up to top
    account_btn.send_keys(Keys.PAGE_UP)
    account_btn.click()
    time.sleep(2)
    driver.find_element(*ACCOUNT_LINK).click()

    # Scrap account data
    driver.switch_to.window(driver.window_handles[1])
    wait.until(EC.visibility_of_element_located(ACCOUNT_ACC_NO))
    account_no = driver.find_element(*ACCOUNT_ACC_NO).text
    account_email = driver.find_element(*ACCOUNT_EMAIL).text

    account_details = {'account_no': account_no, 'email': account_email}

    with open('account_details.json', 'w') as file:
        json.dump(account_details, file)


if __name__ == '__main__':
    login()
    scrap_articles()
    scrap_account_info()
    driver.quit()
    print('Scrapping finished.')
