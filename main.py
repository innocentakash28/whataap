import time
from datetime import datetime
import os
import pyautogui as pt
from selenium import webdriver


driver = webdriver.Chrome(CHROMEDRIVER_PATH)
driver.get('https://web.whatsapp.com/')
# time.sleep(30)
while True:
    try:
        time.sleep(1)

        now = datetime.now()


        driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span')

        current_time = now.strftime("%H:%M:%S")
        file = open('demo.txt', 'a')

        file.write(current_time+ '\n')
        file.close()
        print("Current Time =", current_time)


    except:
        time.sleep(1)


