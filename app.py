from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from random import *
# from os import open

is_headless = False

options = Options()
options.headless = is_headless
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
actions = ActionChains(driver)

for i in range(1,5000):
  driver.get(f"https://whitney.org/collection/works/{i}")
  driver.execute_script(open("./scripts/filter.js").read())
  driver.execute_script(open("./scripts/monitor.js").read())
  driver.execute_script(open("./scripts/vibrate.js").read())
  # sleep(random())
  try:
    driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight / {randint(1,10)});")
    artist_name_ele = driver.find_element_by_css_selector("h2.body-medium-bold.m-0 a")
    artist_name = artist_name_ele.get_attribute("innerHTML")
    print("ARTIST:", artist_name)
    driver.execute_script(f"document.querySelector('#monitor-div').innerHTML = document.querySelector('#monitor-div').innerHTML + '<li>ARTIST: {artist_name}</li>'")
    sleep(random())
  except:
    print("no artist name found")

  try:
    driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight / {randint(1,10)});")
    artwork_name_ele = driver.find_element_by_css_selector("h1.collection-detail-header__title.body-medium.m-0 em")
    artwork_name = artwork_name_ele.get_attribute("innerHTML")
    print("TITLE:", artwork_name)
    driver.execute_script(f"document.querySelector('#monitor-div').innerHTML = document.querySelector('#monitor-div').innerHTML + '<li>TITLE: {artwork_name}</li>'")
    sleep(random())
  except:
    print("no artwork name found")

  try:
    driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight / {randint(1,10)});")
    artwork_year_ele = driver.find_elements_by_css_selector("div.artwork-detail__info p.m-0")[1]
    artwork_year = artwork_year_ele.get_attribute("innerHTML").split("<br>")[1]
    print("YEAR:", artwork_year)
    driver.execute_script(f"document.querySelector('#monitor-div').innerHTML = document.querySelector('#monitor-div').innerHTML + '<li>YEAR: {artwork_year}</li>'")
    driver.execute_script(f"document.querySelector('#monitor-div').innerHTML = document.querySelector('#monitor-div').innerHTML + '<li>YEAR: {artwork_year}</li>'")
    sleep(random())
  except:
    print("no artwork year found!")

driver.quit()
