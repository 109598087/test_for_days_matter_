import datetime
import time

import unittest

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from keywords.open import appium_start_Session
from keywords.wait_until import wait_until_EditActivity_page_is_visible, wait_until_MainActivity_page_is_visible


def click_create_countdown_day_button(self):
    self.driver.find_element_by_accessibility_id("添加新事件").click()
    wait_until_EditActivity_page_is_visible(self)


def click_target_day_button(self):
    self.driver.find_element_by_xpath('//*[@resource-id="com.clover.daysmatter:id/text_due_date"]').click()


def click_set_countdown_book_button(self):
    self.driver.find_element_by_id("com.clover.daysmatter:id/summary_category").click()


def click_countdown_day_set_repeat_button(self):
    self.driver.find_element_by_id("com.clover.daysmatter:id/summary_repeat").click()


def click_blank_space(self):
    try:
        self.driver.tap([(200, 500)], 500)
    except:
        pass


def click_back_button(self):
    time.sleep(2)
    self.driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="向上瀏覽"]').click()


#############################################################
def skip_how_to_use(self):
    self.driver.find_element_by_xpath('//*[@class="android.widget.ImageButton"]').click()
    wait_until_MainActivity_page_is_visible(self)


def input_countdown_day_name(self, countdown_day_name):
    self.driver.find_element_by_id("com.clover.daysmatter:id/text_title").send_keys(countdown_day_name)


# 公陰曆
def click_calendar_type(self):
    self.driver.find_element_by_xpath('//*[@resource-id="com.clover.daysmatter:id/switch_is_lunar_calendar"]').click()


# 只能點畫面上有的
def set_countdown_day_target_day(self, year, month, day):
    click_target_day_button(self)
    self.driver.find_element_by_xpath('//*[contains(@text, "年") and contains(@text, "' + str(year) + '")]').click()
    self.driver.find_element_by_xpath('//*[contains(@text, "月") and contains(@text, "' + str(month) + '")]').click()
    self.driver.find_element_by_xpath('//*[contains(@text, "日") and contains(@text, "' + str(day) + '")]').click()
    click_blank_space(self)


def set_countdown_day_countdown_book(self, countdown_book):
    click_set_countdown_book_button(self)
    time.sleep(1)
    self.driver.find_element_by_xpath(
        '//*[@class="android.widget.TextView" and @resource-id="com.clover.daysmatter:id/list_item_title" and @text=' + '\"' + countdown_book + '\"' + ']').click()


# 置頂
def click_countdown_day_set_top_button(self):
    self.driver.find_element_by_id("com.clover.daysmatter:id/switch_top").click()


# 只能點畫面上有的
def choose_countdown_day_repeat(self, months_years):
    self.driver.find_element_by_xpath('//*[contains(@text, "' + months_years + '")]').click()


def click_save_button(self):
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@resource-id="com.clover.daysmatter:id/button_save"]').click()


def set_countdown_day_repeat(self, countdown_day_repeat):
    time.sleep(1)
    click_countdown_day_set_repeat_button(self)
    time.sleep(1)
    choose_countdown_day_repeat(self, countdown_day_repeat)
    time.sleep(1)
    click_blank_space(self)


def verify_create_countdown_day_successfully(self, countdown_day_name):
    time.sleep(1)
    assert countdown_day_name in self.driver.find_element_by_xpath(
        '//*[contains(@text, ' + countdown_day_name + ')]').get_attribute('name')


def verify_create_countdown_day_unsuccessfully(self, countdown_day_name):
    try:
        self.driver.find_element_by_xpath('//*[contains(@text, ' + countdown_day_name + ')]').get_attribute('name')
    except NoSuchElementException:
        pass
    except StaleElementReferenceException:
        pass


def get_date_of_before(days_of_before):
    today = datetime.datetime.today()
    target_date = today - datetime.timedelta(days_of_before)  # 380天之前
    target_date_str = target_date.strftime("%Y-%m-%d")
    target_date_list = target_date_str.split('-')
    return target_date_list


class TestCountdownDayCreate(unittest.TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.driver = None

    def setUp(self) -> None:
        appium_start_Session(self)
        skip_how_to_use(self)

    def test_create_countdown_day(self):
        click_create_countdown_day_button(self)

        self.countdown_day_name = '123456789'
        target_date_list = get_date_of_before(397)
        self.countdown_day_target_year = int(target_date_list[0])
        self.countdown_day_target_month = int(target_date_list[1])
        self.countdown_day_target_day = int(target_date_list[2])
        self.countdown_day_countdown_book = '工作'
        self.countdown_day_repeat = 'Months'

        input_countdown_day_name(self, self.countdown_day_name)
        set_countdown_day_target_day(self,
                                     self.countdown_day_target_year,
                                     self.countdown_day_target_month,
                                     self.countdown_day_target_day)
        set_countdown_day_countdown_book(self, self.countdown_day_countdown_book)
        # click_countdown_day_set_top_button(self)
        set_countdown_day_repeat(self, self.countdown_day_repeat)
        # 保存
        click_save_button(self)
        verify_create_countdown_day_successfully(self, self.countdown_day_name)
        print('test_create_countdown_day ok')

    def test_create_countdown_day_and_click_back_button(self):
        click_create_countdown_day_button(self)
        self.countdown_day_name = '123456789'
        input_countdown_day_name(self, self.countdown_day_name)
        click_back_button(self)
        verify_create_countdown_day_unsuccessfully(self, self.countdown_day_name)
        print('test_create_countdown_day_and_click_back_button ok')

    def tearDown(self) -> None:
        self.driver.quit()
