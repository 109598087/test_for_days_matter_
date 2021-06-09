# test input :
# name = ''
# target_day =
# 分類
# 置頂
# 重複
# 重複時間
import time

from appium import webdriver
import unittest

from appium.webdriver.common.touch_action import TouchAction

from keywords.open import appium_start_Session
from keywords.wait_until import wait_until_EditActivity_page_is_visible


def click_create_countdown_day_button(self):
    self.driver.find_element_by_accessibility_id("添加新事件").click()
    wait_until_EditActivity_page_is_visible(self)


def input_countdown_day_name(self, countdown_day_name):
    self.driver.find_element_by_id("com.clover.daysmatter:id/text_title").send_keys(countdown_day_name)


def click_target_day_button(self):
    self.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout").click()
    time.sleep(1)


def click_set_class_button(self):
    self.driver.find_element_by_id("com.clover.daysmatter:id/summary_category").click()
    time.sleep(1)


def click_countdown_day_set_top_button(self):
    self.driver.find_element_by_id("com.clover.daysmatter:id/switch_top").click()
    time.sleep(1)


def click_countdown_day_set_repeat_button(self):
    self.driver.find_element_by_id("com.clover.daysmatter:id/summary_repeat").click()
    time.sleep(1)


def click_blank_space(self):
    time.sleep(1)
    try:
        self.driver.tap([(100, 50)], 500)
    except:
        pass
    time.sleep(2)


#############################################################
def skip_how_to_use(self):
    self.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton").click()
    self.driver.wait_activity(".ui.activity.MainActivity", 30)


def set_work_class(self):
    self.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.RelativeLayout").click()


##
def day_choose_countdown_day_yesterday(self):
    e1 = self.driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[3]/android.widget.TextView[2]')
    e2 = self.driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[3]/android.widget.TextView[3]')
    self.driver.drag_and_drop(e1, e2)


##
def choose_repeat_type_every1_weeks(self):
    e1 = self.driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ListView[2]/android.widget.RelativeLayout[3]/android.widget.TextView[1]')
    e2 = self.driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ListView[2]/android.widget.RelativeLayout[4]/android.widget.TextView[1]')
    self.driver.drag_and_drop(e2, e1)


def click_save_button(self):
    self.driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button').click()
    time.sleep(1)


class TestPostCreate(unittest.TestCase):
    def setUp(self) -> None:
        appium_start_Session(self)
        skip_how_to_use(self)

    def test_create_countdown_day(self):
        # 點擊create_countdown_day(+)
        click_create_countdown_day_button(self)
        # 輸入到數日名稱
        countdown_day_name = '123456789'
        input_countdown_day_name(self, countdown_day_name)
        # 設定 target_day -> yesterday
        click_target_day_button(self)
        day_choose_countdown_day_yesterday(self)
        click_blank_space(self)

        # 設定分類
        click_set_class_button(self)
        set_work_class(self)
        # 設定至頂
        # click_countdown_day_set_top_button(self)
        # 設定重複
        click_countdown_day_set_repeat_button(self)
        choose_repeat_type_every1_weeks(self)
        click_blank_space(self)
        # 保存
        click_save_button(self)

        t = self.driver.find_element_by_xpath('//*[contains(@text, ' + countdown_day_name + ')]').get_attribute('name')
        print(t)
        assert countdown_day_name in t

    def tearDown(self) -> None:
        pass
