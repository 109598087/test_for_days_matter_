from appium import webdriver

from keywords.wait_until import wait_until_UserGuideActivity_page_is_visible


def appium_start_Session(self):
    caps = dict()
    caps['deviceName'] = '127.0.0.1:62001'
    caps['platformName'] = 'Android'
    caps['platformVersion'] = '7.1.2'
    caps['appPackage'] = 'com.clover.daysmatter'
    caps['appActivity'] = '.ui.activity.MainActivity'

    # appium start Session
    self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
    self.driver.implicitly_wait(5)
    wait_until_UserGuideActivity_page_is_visible(self)