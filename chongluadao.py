from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import csv
import time
from selenium.webdriver.chrome.options import Options


def crawlData(url):
    links = []

    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.get(url)
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    print('####################### ODD ##########################')
    odds = soup.findAll('tr', class_='odd')
    links += [link.findAll('td')[1] for link in odds]

    print('####################### EVEN ##########################')
    evens = soup.findAll('tr', class_='even')
    links += [link.findAll('td')[1] for link in evens]

    with open('./chongluadao.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        writer.writerow(links)

if __name__ == "__main__":
    crawlData("https://chongluadao.vn/thong-ke")