from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('headless')  # 静默模式
driver = webdriver.Chrome(chrome_options=option)
driver.get("https://www.douban.com/")
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[3]/div/input').send_keys('12345689')
driver.quit()
print('Done')