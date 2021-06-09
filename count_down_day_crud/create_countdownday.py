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
from keywords.wait_until import wait_until_EditActivity_page_is_visible, wait_until_MainActivity_page_is_visible


def click_create_countdown_day_button(self):
    self.driver.find_element_by_accessibility_id("添加新事件").click()
    wait_until_EditActivity_page_is_visible(self)


def click_target_day_button(self):
    self.driver.find_element_by_xpath('//*[@resource-id="com.clover.daysmatter:id/text_due_date"]').click()
    time.sleep(1)


def click_set_class_button(self):
    self.driver.find_element_by_id("com.clover.daysmatter:id/summary_category").click()
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
    self.driver.find_element_by_xpath('//*[@class="android.widget.ImageButton"]').click()
    wait_until_MainActivity_page_is_visible(self)


def input_countdown_day_name(self, countdown_day_name):
    self.driver.find_element_by_id("com.clover.daysmatter:id/text_title").send_keys(countdown_day_name)
    time.sleep(1)


# 公陰曆
def click_calendar_type(self):
    self.driver.find_element_by_xpath('//*[@resource-id="com.clover.daysmatter:id/switch_is_lunar_calendar"]').click()
    time.sleep(1)


# 只能點畫面上有的
def set_countdown_day_target_day(self, year, month, day):
    self.driver.find_element_by_xpath('//*[@text="' + str(year) + '年"]').click()
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@text="' + str(month) + '月"]').click()
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@text="' + str(day) + '日"]').click()
    time.sleep(1)


def set_countdown_day_countdown_book(self, countdown_book):
    self.driver.find_element_by_xpath(
        '//*[@class="android.widget.TextView" and @resource-id="com.clover.daysmatter:id/list_item_title" and @text=' + '\"' + countdown_book + '\"' + ']').click()


# 置頂
def click_countdown_day_set_top_button(self):
    self.driver.find_element_by_id("com.clover.daysmatter:id/switch_top").click()
    time.sleep(1)


# 只能點畫面上有的
def choose_repeat_type_every1_weeks(self, months_years):
    self.driver.find_element_by_xpath('//*[contains(@text, "' + months_years + '")]').click()
    time.sleep(1)


def click_save_button(self):
    self.driver.find_element_by_xpath('//*[@resource-id="com.clover.daysmatter:id/button_save"]').click()
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
        countdown_day_countdown_book = '工作'

        input_countdown_day_name(self, countdown_day_name)
        # 設定 target_day -> yesterday
        click_target_day_button(self)
        set_countdown_day_target_day(self, 2020, 5, 8)
        click_blank_space(self)

        # 設定分類
        click_set_class_button(self)
        set_countdown_day_countdown_book(self, countdown_day_countdown_book)
        # 設定至頂
        # click_countdown_day_set_top_button(self)
        # 設定重複
        click_countdown_day_set_repeat_button(self)
        choose_repeat_type_every1_weeks(self, 'Months')
        click_blank_space(self)
        # 保存
        click_save_button(self)

        t = self.driver.find_element_by_xpath('//*[contains(@text, ' + countdown_day_name + ')]').get_attribute('name')
        print(t)
        assert countdown_day_name in t

    def tearDown(self) -> None:
        pass
