import time
import unittest

from selenium.common.exceptions import NoSuchElementException

from count_down_day_crud.create_countdown_day import skip_how_to_use, click_create_countdown_day_button, \
    input_countdown_day_name, click_save_button
from count_down_day_crud.edit_countdown_day import click_edit_button
from count_down_day_crud.read_countdown_day import read_countdown_day
from keywords.open import appium_start_Session


def delete_countdown_day(self):
    self.driver.find_element_by_xpath('//*[@resource-id="com.clover.daysmatter:id/button_delete"]').click()
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@class="android.widget.Button" and @text="刪除"]').click()


def verify_delete_countdown_day_unsuccessfully(self, countdown_day_name):
    time.sleep(1)
    assert countdown_day_name in self.driver.find_element_by_xpath(
        '//*[contains(@text, ' + countdown_day_name + ')]').get_attribute('name')


class TestPostCreate(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.driver = None

    def setUp(self) -> None:
        appium_start_Session(self)
        skip_how_to_use(self)
        # create countdown_day
        click_create_countdown_day_button(self)
        self.countdown_day_name = '123456789'
        input_countdown_day_name(self, self.countdown_day_name)
        click_save_button(self)

    def test_delete_countdown_day(self):
        # delete countdown_day
        read_countdown_day(self, self.countdown_day_name)
        click_edit_button(self)
        delete_countdown_day(self)
        self.driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="向上瀏覽"]').click()
        try:
            self.driver.find_element_by_xpath(
                '//*[@class="android.widget.TextView" and contains(@text, "' + self.countdown_day_name + '")]')
        except NoSuchElementException:
            pass
        print('test_delete_countdown_day ok')

    def test_delete_countdown_day_and_click_cancel_button(self):
        # delete countdown_day
        read_countdown_day(self, self.countdown_day_name)
        click_edit_button(self)
        self.driver.find_element_by_xpath('//*[@resource-id="com.clover.daysmatter:id/button_delete"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@class="android.widget.Button" and @text="取消"]').click()
        self.driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="向上瀏覽"]').click()
        verify_delete_countdown_day_unsuccessfully(self, self.countdown_day_name)
        print('test_delete_countdown_day_and_click_cancel_button ok')

    def tearDown(self) -> None:
        self.driver.quit()
