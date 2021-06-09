from appium import webdriver
from time import sleep

caps = dict()
caps['deviceName'] = '127.0.0.1:62001'
caps['platformName'] = 'Android'
caps['platformVersion'] = '7.1.2'
caps['appPackage'] = 'com.clover.daysmatter'
caps['appActivity'] = '.ui.activity.MainActivity'

# appium start Session
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)

# ac = driver.wait_activity
# print(ac)

# 跳過HOW TO USE
driver.wait_activity(".ui.activity.UserGuideActivity", 30)  # function化
el1 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton")  # 返回按鈕
el1.click()

driver.wait_activity(".ui.activity.MainActivity", 30)
el2 = driver.find_element_by_accessibility_id("添加新事件")
el2.click()

driver.wait_activity(".ui.activity.EditActivity", 30)
el4 = driver.find_element_by_id("com.clover.daysmatter:id/text_title")
el4.send_keys('')


el5 = driver.find_element_by_id("com.clover.daysmatter:id/button_save")
el5.click()



