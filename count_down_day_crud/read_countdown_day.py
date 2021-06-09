import time
import unittest

from count_down_day_crud.create_countdown_day import skip_how_to_use, click_create_countdown_day_button, \
    set_countdown_day_target_day, input_countdown_day_name, set_countdown_day_countdown_book, set_countdown_day_repeat, \
    click_save_button
from keywords.open import appium_start_Session


def read_countdown_day(self, countdown_day_name):
    self.driver.find_element_by_xpath(
        '//*[@class="android.widget.TextView" and contains(@text, "' + countdown_day_name + '")]').click()
    time.sleep(1)


class TestCountDownRead(unittest.TestCase):
    def setUp(self) -> None:
        appium_start_Session(self)
        skip_how_to_use(self)

    def test_read_countdown_day(self):
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
        # read
        read_countdown_day(self, countdown_day_name)
        assert countdown_day_name in self.driver.find_element_by_xpath(
            '//*[@resource-id="com.clover.daysmatter:id/title"]').get_attribute('name')
        print('test_read_countdown_day ok')

    def tearDown(self) -> None:
        pass
