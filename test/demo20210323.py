from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
import unittest

caps = dict()
caps['deviceName'] = '127.0.0.1:62001'
caps['platformName'] = 'Android'
caps['platformVersion'] = '7.1.2'
caps['appPackage'] = 'com.clover.daysmatter'
caps['appActivity'] = '.ui.activity.MainActivity'

# appium start Session
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)

# 產生wait?
wait = WebDriverWait(driver, 10)

# 開始test
# 跳過HOW TO USE
driver.wait_activity(".ui.activity.UserGuideActivity", 30)  # function化
el1 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton")  # 返回按鈕
el1.click()

# actions = TouchAction(driver)
# actions.scroll(10, 100)

# 點GOOGLE成立已經
driver.wait_activity(".ui.activity.MainActivity", 30)
el2 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.FrameLayout[3]")
el2.click()

driver.wait_activity(".ui.activity.DetailActivity", 30)
el3 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout")
el3.click()

# test id_dispaly()
if driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout').is_displayed():
    print('Run the next process')
