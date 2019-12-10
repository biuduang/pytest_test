#coding=UTF-8
from selenium import webdriver
import time
Options=webdriver.ChromeOptions()
Options.add_argument('--headless')


driver=webdriver.Chrome(options=Options)
driver.get('http://10.1.1.121:81/main/login.html')
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="phone"]').send_keys('15599054321')
driver.find_element_by_xpath('//*[@id="password"]').send_keys(111111)
driver.find_element_by_xpath('//*[@id="login"]').click()
time.sleep(3)
print(driver.current_url)
