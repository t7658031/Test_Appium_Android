from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

def get_tracks(distance):
    v = 0
    t= 0.3
    tracks = []
    current = 0
    mid = distance*4/5
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        s = v0*t+0.5*a*(t**2)
        current += s
        tracks.append(round(s))
        v = v0 + a*t
    return tracks

driver = webdriver.Chrome()
driver.get('https://mx80.bet/')

sleep(5)
#driver.find_element_by_xpath('//div[1]/div[1]/ul[1]/li[2]').click()
#driver.switch_to.frame(0)
driver.find_element_by_xpath('/html/body/section/header/div[1]/div/div[3]/button[1]').click()
driver.find_element_by_xpath('/html/body/section/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys('t11234567')
driver.find_element_by_xpath('/html/body/section/div[3]/div/div[2]/form/div[2]/div/div[1]/input').send_keys('test123')
driver.find_element_by_xpath('/html/body/section/div[3]/div/div[2]/div[3]/button/span').click()
#driver.find_element_by_css_selector('div.anony-nav-links ul li:nth-child(5)').click()
#driver.quit() /html/body/div[1]/div[1]/ul[1]/li[2]
sleep(20)
#driver.switch_to.frame(0)
#element = driver.find_element_by_xpath('//html/body/section/div[3]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[1]/img')
element = driver.find_element_by_xpath('//*[@id="dx_captcha_basic_slider-img-normal_1"]')
actions = ActionChains(driver)
actions.click_and_hold(element).perform()
actions.move_to_element_with_offset(element, xoffset=142, yoffset=0).perform()
actions.release().perform()

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