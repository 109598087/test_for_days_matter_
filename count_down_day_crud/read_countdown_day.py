import unittest

from count_down_day_crud.create_countdown_day import skip_how_to_use, click_create_countdown_day_button, \
    input_countdown_day_name, click_save_button
from keywords.open import appium_start_Session


def read_countdown_day(self, countdown_day_name):
    self.driver.find_element_by_xpath(
        '//*[@class="android.widget.TextView" and contains(@text, "' + countdown_day_name + '")]').click()


def verify_read_countdown_day_successfully(self, countdown_day_name):
    assert countdown_day_name in self.driver.find_element_by_xpath(
        '//*[@resource-id="com.clover.daysmatter:id/title"]').get_attribute('name')


def click_countdown_day(self):
    self.driver.find_element_by_xpath(
        '//*[@resource-id="com.clover.daysmatter:id/date"]')


def verify_change_read_date_format_successfully(self):
    print(self.driver.find_element_by_xpath(
        '//*[@resource-id="com.clover.daysmatter:id/date"]').get_attribute('name'))
    assert '天' in self.driver.find_element_by_xpath(
        '//*[@resource-id="com.clover.daysmatter:id/date"]').get_attribute('name')


class TestCountDownRead(unittest.TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.driver = None

    def setUp(self) -> None:
        appium_start_Session(self)
        skip_how_to_use(self)
        # create a_countdown_day
        click_create_countdown_day_button(self)
        self.countdown_day_name = 'countdown_day_name'
        input_countdown_day_name(self, self.countdown_day_name)
        click_save_button(self)

    def test_read_countdown_day(self):
        # read
        read_countdown_day(self, self.countdown_day_name)
        verify_read_countdown_day_successfully(self, self.countdown_day_name)
        # click_countdown_day(self)
        # verify_change_read_date_format_successfully(self)
        print('test_read_countdown_day ok')

    def tearDown(self) -> None:
        self.driver.quit()
