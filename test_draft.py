import os
from time import sleep,time
from time import strftime, localtime
import logging
#import appium
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
import pandas as pd

num = 4
for n in range(num):
    i = input("test\n")
    #print(i)
    j = [i]
    k = {"test":j}
    df1=pd.DataFrame(k)
    #print(df)
    data=df.append(k,ignore_index=True)
    print(data)


