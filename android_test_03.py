import unittest
from appium import webdriver
import os
from time import sleep,time
from time import strftime, localtime
import logging
#import appium
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
import pandas as pd


class MyTestCase(unittest.TestCase):
 #def test_something(self):
    #elf.assertEqual(True, False)

 def setUp(self):
    desired_caps = {
                'platformName': 'Android',
                #'platformVersion': '5.1.1',
                'platformVersion': '8.0.0',
                #'deviceName': '127.0.0.1:62001',
                'deviceName': 'H4AZCY00A2824UE',
                #'app': 'D:/Api/0106/mx2main_142.apk',
                'appPackage': 'com.btcbet.main',
                'appActivity': 'com.btcbet.main.mvp.ui.activity.host.ChooseHostActivity',
                #'unid': '127.0.0.1:62001'
                'unid': 'H4AZCY00A2824UE',
                'newCommandTimeout': '6000',
                 }
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    sleep(5)

 def tearDown(self):
    self.driver.quit()
    print('Eddy_test_scenario: Done')


 def test_Name(self):
    print('Eddy_test_scenario: Start')
    sleep(10)
    self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
    sleep(10)
    self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
    #self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
    sleep(20)
    #if (self.driver.find_element_by_id("com.btcbet.main:id/next")):
    #    self.driver.find_element_by_id("com.btcbet.main:id/next").click()
    #else:
    #    print("None")
    #sleep(8)
    self.driver.find_element_by_xpath("//*[@text='彩票']").click()
    sleep(10)
    self.driver.find_element_by_xpath("//*[@text='万博NY彩票']").click()
    sleep(10)
    print("USER PASSWORD")
    self.driver.find_element_by_id("com.btcbet.main:id/nameEt").send_keys('t7658031')
    self.driver.find_element_by_id("com.btcbet.main:id/passwordEt").send_keys('a1234567')
    self.driver.find_element_by_id("com.btcbet.main:id/savePasswordBtn").click()
    self.driver.find_element_by_id("com.btcbet.main:id/loginBtn").click()
    sleep(20)
    print("Please verify the image\n")
    input()
    #self.driver.switch_to.frame(0)
    #element = self.driver.find_element_by_id('dx_captcha_basic_slider-img-normal_1')
    #TouchAction(driver).press(element).move_to(element,282,0).perform()
    #ActionChains(driver).move_to_element_with_offset(to_element=element, xoffset=282, yoffset=0).perform()
    #ActionChains(driver).pause(2).release(element).perform()
    print("TEST_PORINT")
    sleep(10)
    print("Eddy_TP00")
    sleep(10)
    print("Eddy_TP01")
    flag_1 = MyTestCase.isElementExist_id(self, "com.btcbet.main:id/meIv")
    flag_2 = MyTestCase.isElementExist_xpath(self, "//*[@text='Access Denied Error 403']")
    flag_3 = MyTestCase.isElementExist_xpath(self, "//*[@text='万博NY彩票']")
    flag_4 = MyTestCase.isElementExist_xpath(self, "//*[@text='万博VR彩票']")
    print(flag_1)
    print(flag_2)
    print(flag_3)
    try:
        pass_game1 = 0
        pass_game2 = 0
        while flag_1:
            number = 5
            for i in range(number):
                print("Login Successifully")
                print("i:",i)
                sleep(10)
                self.driver.find_element_by_xpath("//*[@text='彩票']").click()
                sleep(10)
                self.driver.find_element_by_xpath("//*[@text='万博NY彩票']").click()
                sleep(20)
                print(flag_3)
                # self.driver.switch_to.frame(0)
                if flag_3 == True:
                    pass_game1 = pass_game1 + 1
                    MyTestCase.take_screenShot(self,"Eddy_TS_01")
                    print("pass_game1:", pass_game1)
                    #self.driver.find_element_by_id("com.btcbet.main:id/toolbar_close").click()
                    self.driver.keyevent(4)
                else:
                    #self.driver.find_element_by_id("com.btcbet.main:id/toolbar_close").click()
                    self.driver.keyevent(4)
                sleep(10)
                self.driver.find_element_by_xpath("//*[@text='万博VR彩票']").click()
                sleep(20)
                if flag_4 == True:
                    pass_game2 = pass_game2 + 1
                    MyTestCase.take_screenShot(self,"Eddy_TS_02")
                    print("pass_game2:", pass_game2)
                    #self.driver.find_element_by_id("com.btcbet.main:id/toolbar_close").click()
                    self.driver.keyevent(4)
                else:
                    #self.driver.find_element_by_id("com.btcbet.main:id/toolbar_close").click()
                    self.driver.keyevent(4)
                sleep(15)
                print("pass_game1,pass_game2:", pass_game1, pass_game2)
                pass_game_ny = [pass_game1]
                pass_game_vr = [pass_game2]
                print(pass_game_ny)
                print(pass_game_vr)
                dic = {
                    "PNY" : pass_game_ny,
                    "PVR" : pass_game_vr
                }
                df = pd.DataFrame(dic)
                print(df)
                if i == 0:
                    df.to_csv('test.csv',mode='a',index=None,header=True)
                    dfr_1 = pd.read_csv('test.csv', sep=',', encoding='gbk')
                    print('dfr_1:',dfr_1)
                else:
                    df.to_csv('test.csv', mode='a', index=None, header=False)
                    dfr_2 = pd.read_csv('test.csv', sep=',', encoding='gbk')
                    print("dfr_2:",dfr_2)
        # else:
        #    print("Login Unsuccessifully")
    except Exception:
        print("Login Unsuccessifully")
    else:
        self.driver.keyevent(3)
        print("Test Done")
        # self.driver.find_element_by_xpath("//*[@text='万博VR彩票']").click()
        # sleep(30)
        # self.driver.find_element_by_id("com.nextmediatw:id/phone_number_input_text").send_keys('978290522')
        # sleep(30)
        # self.driver.find_element_by_id("com.nextmediatw:id/sms_login_btn").click()
        # sleep(30)

 def isElementExist_xpath(self, testelement_xpath):
     flag = False
     #browser = self.driver
     try:
         self.driver.find_elements_by_xpath(testelement_xpath)
         flag = True
         return flag
     except:
         #flag = False
         return flag

 def isElementExist_id(self, testelement_id):
     flag = False
     #browser = self.driver
     try:
         self.driver.find_element_by_id(testelement_id)
         print("Eddy_TP0A")
         flag = True
         return flag
     except:
         #flag = False
         return flag

 def take_screenShot(self, name):
     day = strftime("%Y-%m-%d", localtime(time()))
     fq = "..\\screenShots\\" + day
     print("Eddy_TPB01:%s",fq)
     # fq =os.getcwd()[:-4] +'screenShots\\'+day    根据获取的路径，然后截取路径保存到自己想存放的目录下
     tm = strftime("%Y-%m-%d_%H_%M_%S", localtime(time()))
     type = '.png'
     filename = ""
     if os.path.exists(fq):
         filename = fq + "\\" + tm + "_" + name + type
         print(filename)
     else:
         os.makedirs(fq)
         filename = fq + "\\" + tm + "_" + name + type
         print(filename)
     # c = os.getcwd()
     # r"\\".join(c.split("\\"))     #此2行注销实现的功能为将路径中的\替换为\\
     self.driver.get_screenshot_as_file(filename)


if __name__ == '__main__':
    unittest.main()
