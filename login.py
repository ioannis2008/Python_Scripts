from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import By
import time

url = 'https://instargram.com/login/'

browser = webdriver.Firefox
browser.get(url)
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,\
    '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]'))).click()


time.sleep(4)

file = open ('pass.txt', 'r')
password = file.readlines()
browser.find_element(By.NAME, 'username').send_keys('p4pasopoulouu._')
browser.find_element(By.NAME, 'password').send_keys(password)
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,\
    '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div/div[3]/button'))).click()
time.sleep(2000)
browser.close()


