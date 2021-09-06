import csv
import time
from time import sleep
from random import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# is_headless = False

# options = Options()
# options.headless = is_headless
# options.add_argument("--window-size=1920,1200")

# DRIVER_PATH = '/usr/local/bin/chromedriver'
# driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
# actions = ActionChains(driver)

# missing_count = 0
# i = 0


my_dict = {"test": 1, "testing": 2}
my_dict_2 = {"test": 3, "testing": 4}

count_2 = 0

# new output csv file params
csv_id = hex(int(time.time()))
data_filepath = f"data/whitney_artworks_data_{csv_id}.csv"

with open(data_filepath, 'w') as f:
  w = csv.DictWriter(f, my_dict.keys())
  w.writeheader()

while True:
  with open(data_filepath, 'a') as f: 
    w = csv.DictWriter(f, my_dict.keys())
    w.writerow({"test": count_2, "testing": count_2 + 1})
    count_2 += 2
    sleep(1)


# with open('mycsvfile.csv', 'w') as f:  # You will need 'wb' mode in Python 2.x
#     # w = csv.DictWriter(f, my_dict.keys())
#     # w.writeheader()
#     # w.writerow(my_dict)
    
#     w2 = csv.DictWriter(f, my_dict_2.keys())
#     # w.writeheader()
#     w2.writerow(my_dict_2)



# while missing_count < 10:
#   temp_count = 0
#   driver.get(f"https://whitney.org/collection/works/{i}")
#   driver.execute_script(open("./scripts/filter.js").read())
#   driver.execute_script(open("./scripts/monitor.js").read())
#   driver.execute_script(open("./scripts/vibrate.js").read())
#   try:
#     driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight / {randint(1,10)});")
#     artist_name_ele = driver.find_element_by_css_selector("h2.body-medium-bold.m-0 a")
#     artist_name = artist_name_ele.get_attribute("innerHTML")
#     print("artist_name:", artist_name)
#     driver.execute_script(f"document.querySelector('#monitor-div').innerHTML = document.querySelector('#monitor-div').innerHTML + '<li>artist_name: {artist_name}</li>'")
#     sleep(random())
#   except:
#     temp_count += 1
#     print("no artist name found")

#   try:
#     driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight / {randint(1,10)});")
#     artwork_name_ele = driver.find_element_by_css_selector("h1.collection-detail-header__title.body-medium.m-0 em")
#     artwork_name = artwork_name_ele.get_attribute("innerHTML")
#     print("artwork_name:", artwork_name)
#     driver.execute_script(f"document.querySelector('#monitor-div').innerHTML = document.querySelector('#monitor-div').innerHTML + '<li>artwork_name: {artwork_name}</li>'")
#     sleep(random())
#   except:
#     temp_count += 1
#     print("no artwork name found")

#   try:
#     driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight / {randint(1,10)});")
#     artwork_year_ele = driver.find_elements_by_css_selector("div.artwork-detail__info p.m-0")[1]
#     artwork_year = artwork_year_ele.get_attribute("innerHTML").split(">")[-1]
#     print("artwork_year:", artwork_year)
#     driver.execute_script(f"document.querySelector('#monitor-div').innerHTML = document.querySelector('#monitor-div').innerHTML + '<li>artwork_year: {artwork_year}</li>'")
#     sleep(random())
#   except:
#     temp_count += 1
#     print("no artwork year found!")

#   try:
#     driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight / {randint(1,10)});")
#     artwork_classification_ele = driver.find_element_by_css_selector("div.artwork-detail__info p.m-0 a")
#     artwork_classification = artwork_classification_ele.get_attribute("innerHTML")
#     print("artwork_classification:", artwork_classification)
#     driver.execute_script(f"document.querySelector('#monitor-div').innerHTML = document.querySelector('#monitor-div').innerHTML + '<li>artwork_classification: {artwork_classification}</li>'")
#     sleep(random())
#   except:
#     temp_count += 1
#     print("no artwork_classification found!")

#   try:
#     driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight / {randint(1,10)});")
#     artwork_medium_ele = driver.find_elements_by_css_selector("div.artwork-detail__info p.m-0 a")[1]
#     artwork_medium = artwork_medium_ele.get_attribute("innerHTML")
#     print("artwork_medium:", artwork_medium)
#     driver.execute_script(f"document.querySelector('#monitor-div').innerHTML = document.querySelector('#monitor-div').innerHTML + '<li>artwork_medium: {artwork_medium}</li>'")
#     sleep(random())
#   except:
#     temp_count += 1
#     print("no artwork_medium found!")

#   try:
#     driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight / {randint(1,10)});")
#     artwork_dimensions_ele = driver.find_elements_by_css_selector("div.artwork-detail__info p.m-0")[4]
#     artwork_dimensions = artwork_dimensions_ele.get_attribute("innerHTML").split(">")[-1]
#     print("artwork_dimensions:", artwork_dimensions)
#     driver.execute_script(f"document.querySelector('#monitor-div').innerHTML = document.querySelector('#monitor-div').innerHTML + '<li>artwork_dimensions: {artwork_dimensions}</li>'")
#     sleep(random())
#   except:
#     temp_count += 1
#     print("no artwork_dimensions found!")

#   try:
#     driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight / {randint(1,10)});")
#     artwork_image_url_ele = driver.find_element_by_css_selector("img.artwork")
#     artwork_image_url = artwork_image_url_ele.get_attribute("src")
#     print("artwork_image_url:", artwork_image_url)
#     driver.execute_script(f"document.querySelector('#monitor-div').innerHTML = document.querySelector('#monitor-div').innerHTML + '<li>artwork_image_url: {artwork_image_url}</li>'")
#     sleep(random())
#   except:
#     temp_count += 1
#     print("no artwork_image_url found!")

#   if temp_count == 0:
#     missing_count = 0
#   else:
#     missing_count += 1

#   driver.execute_script(f"document.querySelector('#monitor-div').innerHTML = document.querySelector('#monitor-div').innerHTML + '<li>-- artwork_{i} complete --</li>'")
#   print(f"-- artwork_{i} complete --")
#   sleep(random())

#   i += 1

# driver.quit()
