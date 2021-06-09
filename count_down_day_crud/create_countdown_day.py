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
from selenium.common.exceptions import NoSuchElementException

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
    click_target_day_button(self)
    self.driver.find_element_by_xpath('//*[@text="' + str(year) + '年"]').click()
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@text="' + str(month) + '月"]').click()
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@text="' + str(day) + '日"]').click()
    time.sleep(1)
    click_blank_space(self)


def set_countdown_day_countdown_book(self, countdown_book):
    click_set_class_button(self)
    self.driver.find_element_by_xpath(
        '//*[@class="android.widget.TextView" and @resource-id="com.clover.daysmatter:id/list_item_title" and @text=' + '\"' + countdown_book + '\"' + ']').click()
    time.sleep(1)


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


def set_countdown_day_repeat(self, countdown_day_repeat):
    click_countdown_day_set_repeat_button(self)
    choose_repeat_type_every1_weeks(self, countdown_day_repeat)
    click_blank_space(self)


def verify_create_countdown_day_successfully(self, countdown_day_name):
    assert countdown_day_name in self.driver.find_element_by_xpath(
        '//*[contains(@text, ' + countdown_day_name + ')]').get_attribute('name')


def verify_create_countdown_day_unsuccessfully(self, countdown_day_name):
    try:
        self.driver.find_element_by_xpath('//*[contains(@text, ' + countdown_day_name + ')]').get_attribute('name')
    except NoSuchElementException:
        pass


class TestPostCreate(unittest.TestCase):
    def setUp(self) -> None:
        appium_start_Session(self)
        skip_how_to_use(self)

    def test_create_countdown_day(self):
        click_create_countdown_day_button(self)
        # 輸入到數日名稱
        countdown_day_name = '123456789'
        countdown_day_target_year = 2020
        countdown_day_target_month = 5
        countdown_day_target_day = 8
        countdown_day_countdown_book = '工作'
        countdown_day_repeat = 'Months'

        input_countdown_day_name(self, countdown_day_name)
        set_countdown_day_target_day(self, countdown_day_target_year, countdown_day_target_month,
                                     countdown_day_target_day)
        set_countdown_day_countdown_book(self, countdown_day_countdown_book)
        # click_countdown_day_set_top_button(self)
        set_countdown_day_repeat(self, countdown_day_repeat)
        # 保存
        click_save_button(self)
        verify_create_countdown_day_successfully(self, countdown_day_name)
        print('test_create_countdown_day ok')

    def test_create_countdown_day_and_click_back_button(self):
        click_create_countdown_day_button(self)
        # 輸入到數日名稱
        countdown_day_name = '123456789'
        input_countdown_day_name(self, countdown_day_name)

        self.driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="向上瀏覽"]').click()
        time.sleep(1)
        verify_create_countdown_day_unsuccessfully(self, countdown_day_name)
        print('test_create_countdown_day_and_click_back_button ok')

    def tearDown(self) -> None:
        pass
