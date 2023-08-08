from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from databases.db import Team

service = Service(executable_path='drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://www.scrapethissite.com/pages/forms/?page_num=1')

team = Team()
while True:
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    for tr in soup.select('tr.team'):
        name = tr.select_one('td.name').text.strip()
        year = int(tr.select_one('td.year').text.strip())
        wins = int(tr.select_one('td.wins').text.strip())
        losses = int(tr.select_one('td.losses').text.strip())
        pct = float(tr.select_one('td.pct').text.strip())
        team.insert(name, year, wins, losses, pct)

    try:
        a_next = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Next"]')
        a_next.click()
    except:
        break


    