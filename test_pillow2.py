import time,random
from PIL import Image
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
URL = 'https://account.ch.com/NonRegistrations-Regist'
driver.get(URL)
username = '16574488587'
pwd = 'test1234'
sleep(2)
#driver.switch_to.frame(0)
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[4]/div[2]/div[1]/input').send_keys(username)
print(username,pwd)
driver.find_element_by_xpath('//*[@id="getDynamicPwd"]').click()
#driver.switch_to.frame(0)
sleep(2)
element = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[6]/div/div[1]/div[2]/div[2]')
ActionChains(driver).click_and_hold(on_element = element).perform()
sleep(0.05)
ActionChains(driver).move_to_element_with_offset(to_element= element, xoffset=85  , yoffset=0).perform()
sleep(0.05)
ActionChains(driver).pause(0.1).release(element).perform()
sleep(5)
print('tag0')
ActionChains(driver).click_and_hold(on_element = element).perform()
sleep(0.05)
ActionChains(driver).move_to_element_with_offset(to_element= element, xoffset=105  , yoffset=0).perform()
sleep(0.05)
ActionChains(driver).pause(0.1).release(element).perform()
sleep(5)
print('tag1')
ActionChains(driver).click_and_hold(on_element = element).perform()
sleep(0.05)
ActionChains(driver).move_to_element_with_offset(to_element= element, xoffset=125  , yoffset=0).perform()
sleep(0.05)
ActionChains(driver).pause(0.1).release(element).perform()
sleep(5)
print('tag2')
ActionChains(driver).click_and_hold(on_element = element).perform()
sleep(0.05)
ActionChains(driver).move_to_element_with_offset(to_element= element, xoffset=145  , yoffset=0).perform()
sleep(0.05)
ActionChains(driver).pause(0.1).release(element).perform()
sleep(5)
print('tag3')
ActionChains(driver).click_and_hold(on_element = element).perform()
sleep(0.05)
ActionChains(driver).move_to_element_with_offset(to_element= element, xoffset=205 , yoffset=0).perform()
sleep(0.05)
ActionChains(driver).pause(0.1).release(element).perform()
sleep(5)
print('tag4')
ActionChains(driver).click_and_hold(on_element = element).perform()
sleep(0.05)
ActionChains(driver).move_to_element_with_offset(to_element= element, xoffset=65 , yoffset=0).perform()
sleep(0.05)
ActionChains(driver).pause(0.1).release(element).perform()
sleep(5)
print('tag5')