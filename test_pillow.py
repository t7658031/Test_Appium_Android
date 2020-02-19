from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
URL = 'https://www.douban.com/'
driver.get(URL)
username = 't1123456789'
pwd = 'test1234'
sleep(2)
driver.switch_to.frame(0)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(pwd)
print(username,pwd)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
#driver.switch_to.frame(0)
sleep(2)

#driver.find_element_by_xpath('/html/body/section/header/div[1]/div/div[3]/button[1]').click()
#driver.find_element_by_xpath('/html/body/section/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys('t11234567')
#driver.find_element_by_xpath('/html/body/section/div[3]/div/div[2]/form/div[2]/div/div[1]/input').send_keys('test123')
#driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
#driver.find_element_by_css_selector('div.anony-nav-links ul li:nth-child(5)').click()
#driver.quit() /html/body/div[1]/div[1]/ul[1]/li[2]
#sleep(2)
#image = driver.find_element_by_xpath('//*[@id="slideBkg"]')
#driver.switch_to.frame(0)
#element = driver.find_element_by_xpath('//html/body/section/div[3]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[1]/img')
driver.switch_to.frame(0)
element = driver.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
ActionChains(driver).click_and_hold(on_element = element).perform()
sleep(0.05)
ActionChains(driver).move_to_element_with_offset(to_element= element, xoffset=185  , yoffset=0).perform()
sleep(0.05)
#tracks = get_tracks(2)
#for track in tracks:
#    actions.move_by_offset(xoffset=track, yoffset=0).perform()
#sleep(1)
ActionChains(driver).pause(1).release().perform()
ActionChains(driver).click_and_hold(on_element = element).perform()
ActionChains(driver).move_to_element_with_offset(to_element= element, xoffset=195  , yoffset=0).perform()
ActionChains(driver).pause(1).release().perform()
sleep(0.05)
ActionChains(driver).click_and_hold(on_element = element).perform()
ActionChains(driver).move_to_element_with_offset(to_element= element, xoffset=205  , yoffset=0).perform()
ActionChains(driver).pause(1).release().perform()
sleep(0.05)
ActionChains(driver).click_and_hold(on_element = element).perform()
ActionChains(driver).move_to_element_with_offset(to_element= element, xoffset=217  , yoffset=0).perform()
ActionChains(driver).pause(1).release().perform()
#actions.release().perform()
#actions.click_and_hold(on_element = element).perform()
#sleep(3)
#actions.move_to_element_with_offset(to_element= element, xoffset=172  , yoffset=0).perform()
#sleep(3)
#actions.click()
#actions.release().perform()
#ActionChains(driver).click_and_hold(on_element= element).perform()
#ActionChains(driver).move_to_element_with_offset(to_element= element, xoffset=50, yoffset=0).perform()
#ActionChains(driver).release().perform()
#//*[@id="dx_captcha_basic_btn-refresh_1"]
#//*[@id="dx_captcha_basic_slider-img-normal_1"]
#//*[@id="dx_captcha_basic_slider-img-animated-wrap_1"]/span[4]
#//*[@id="dx_captcha_basic_slider-img-animated-wrap_1"]/span[4]
#/html/body/section/div[3]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[1]/img


print('Done')

#/html/body/div[1]/div[1]/ul[1]/li[2]
#//*[@id="anony-nav"]/div[1]/ul/li[2]/a
#/html/body/div[1]/div[2]/div[1]/div[3]/div/input

#body > div.account-body.login-wrap.login-start.account-anonymous > div.account-body-tabs > ul.tab-start > li.account-tab-account
#driver.find_element_by_css_selector('body div[class="account-body.login-wrap.login-start.account-anonymous"] div[class="account-body-tabs"] ul[class="tab-start"] li[class="account-tab-account"]').click
#//*[@id="anony-nav"]/div[1]/ul/li[5]/a
#anony-nav > div.anony-nav-links > ul > li:nth-child(5) > a
#body > div.account-body.login-wrap.login-start.account-anonymous > div.account-body-tabs > ul.tab-start > li.account-tab-account.on