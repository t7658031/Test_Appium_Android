import unittest
from appium import webdriver
import os
from time import sleep
import logging


class MyTestCase(unittest.TestCase):
 #def test_something(self):
    #elf.assertEqual(True, False)

 def setUp(self):
    desired_caps = {'platformName': 'Android',
                'platformVersion': '8.0.0',
                'deviceName': 'H4AZCY00A2824UE',
                'app': 'D:/Work Log/apple.apk',
                'appPackage': 'com.nextmediatw',
                'appActivity':   'com.nextmedia.activity.SplashScreenActivity',
                'unid':'H4AZCY00A2824UE'
                    }
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    sleep(15)

 def tearDown(self):
    self.driver.quit()
    print('Eddy_test_scenario: Done')

 def test_Name(self):
    print('Eddy_test_scenario: Start')
    sleep(30)
    #self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
    #sleep(15)
    self.driver.find_element_by_id("com.nextmediatw:id/btn_no_show_again").click()
    sleep(30)
    self.driver.press_keycode(5)
    sleep(30)
    self.driver.find_element_by_id("com.nextmediatw:id/ivLoginProfile").click()
    sleep(30)
    self.driver.find_element_by_id("com.nextmediatw:id/phone_number_input_text").send_keys('978290522')
    sleep(30)
    self.driver.find_element_by_id("com.nextmediatw:id/sms_login_btn").click()
    sleep(30)



if __name__ == '__main__':
    unittest.main()
