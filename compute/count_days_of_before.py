import datetime
import time
import unittest

from count_down_day_crud.create_countdown_day import skip_how_to_use
from keywords.open import appium_start_Session


def click_menu_botton(self):
    self.driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Open the main menu"]').click()


def click_countdown_book_button(self):
    self.driver.find_element_by_xpath('//*[@class="android.widget.RelativeLayout"]').click()


def click_data_calculator_button(self):
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@text="Date Calculator"]').click()


def input_before_date_num(self, before_date_num):
    self.driver.find_element_by_xpath('//*[@resource-id="com.clover.daysmatter:id/before_date_num"]').send_keys(
        before_date_num)


class TestCountDaysOfBefore(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.driver = None

    def setUp(self) -> None:
        appium_start_Session(self)
        skip_how_to_use(self)

    def test_count_days_before_input1(self):
        click_menu_botton(self)
        click_countdown_book_button(self)
        click_data_calculator_button(self)
        before_date_num = 2
        input_before_date_num(self, before_date_num)

        threeDayAgo = datetime.datetime.today() - datetime.timedelta(before_date_num)
        otherStyleTime = threeDayAgo.strftime("%Y-%m-%d")
        assert otherStyleTime in self.driver.find_element_by_xpath('//*[contains(@text, "公元")]').get_attribute('name')
        print('test_count_days_before_input1 ok')

    def test_count_days_before_input2(self):
        click_menu_botton(self)
        click_countdown_book_button(self)
        click_data_calculator_button(self)
        before_date_num = 100
        input_before_date_num(self, before_date_num)

        threeDayAgo = datetime.datetime.today() - datetime.timedelta(before_date_num)
        otherStyleTime = threeDayAgo.strftime("%Y-%m-%d")
        assert otherStyleTime in self.driver.find_element_by_xpath('//*[contains(@text, "公元")]').get_attribute('name')
        print('test_count_days_before_input2 ok')

    def test_count_days_before_input3(self):
        click_menu_botton(self)
        click_countdown_book_button(self)
        click_data_calculator_button(self)
        before_date_num = 1000
        input_before_date_num(self, before_date_num)

        threeDayAgo = datetime.datetime.today() - datetime.timedelta(before_date_num)
        otherStyleTime = threeDayAgo.strftime("%Y-%m-%d")
        assert otherStyleTime in self.driver.find_element_by_xpath('//*[contains(@text, "公元")]').get_attribute('name')
        print('test_count_days_before_input3 ok')

    def test_count_days_before_input4(self):
        click_menu_botton(self)
        click_countdown_book_button(self)
        click_data_calculator_button(self)
        before_date_num = 10000
        input_before_date_num(self, before_date_num)

        threeDayAgo = datetime.datetime.today() - datetime.timedelta(before_date_num)
        otherStyleTime = threeDayAgo.strftime("%Y-%m-%d")
        assert otherStyleTime in self.driver.find_element_by_xpath('//*[contains(@text, "公元")]').get_attribute('name')
        print('test_count_days_before_input4 ok')

    def tearDown(self) -> None:
        self.driver.quit()
