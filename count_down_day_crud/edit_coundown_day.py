import time
import unittest

from count_down_day_crud.create_countdown_day import skip_how_to_use, click_create_countdown_day_button, \
    input_countdown_day_name, set_countdown_day_target_day, set_countdown_day_countdown_book, set_countdown_day_repeat, \
    click_save_button, click_countdown_day_set_top_button
from count_down_day_crud.read_countdown_day import read_countdown_day
from keywords.open import appium_start_Session


def click_edit_button(self):
    self.driver.find_element_by_xpath('//android.widget.TextView[@content-desc="編輯"]').click()
    time.sleep(1)


def verify_edit_countdown_day_successfully(self, countdown_day_name, countdown_day_target_year,
                                           countdown_day_target_month,
                                           countdown_day_target_day):
    assert countdown_day_name in self.driver.find_element_by_xpath(
        '//*[@resource-id="com.clover.daysmatter:id/title"]').get_attribute('name')
    assert str(countdown_day_target_year) in self.driver.find_element_by_xpath(
        '//*[contains(@text, "目標日")]').get_attribute('name')
    assert str(countdown_day_target_month) in self.driver.find_element_by_xpath(
        '//*[contains(@text, "目標日")]').get_attribute('name')
    assert str(countdown_day_target_day) in self.driver.find_element_by_xpath(
        '//*[contains(@text, "目標日")]').get_attribute('name')


class TestCountdownDayEdit(unittest.TestCase):
    def setUp(self) -> None:
        appium_start_Session(self)
        skip_how_to_use(self)

    def test_edit_a_countdown_day_with_input1(self):
        # create a_countdown_day
        click_create_countdown_day_button(self)
        # 輸入到數日名稱
        countdown_day_name = 'countdown_day_name'
        input_countdown_day_name(self, countdown_day_name)
        # 保存
        click_save_button(self)

        # edit
        read_countdown_day(self, countdown_day_name)
        click_edit_button(self)

        countdown_day_target_year = 2021
        countdown_day_target_month = 6
        countdown_day_target_day = 9
        countdown_day_countdown_book = '工作'
        countdown_day_repeat = 'Weeks'

        set_countdown_day_target_day(self, countdown_day_target_year, countdown_day_target_month,
                                     countdown_day_target_day)
        set_countdown_day_countdown_book(self, countdown_day_countdown_book)
        click_countdown_day_set_top_button(self)
        set_countdown_day_repeat(self, countdown_day_repeat)
        # 保存
        click_save_button(self)

        verify_edit_countdown_day_successfully(self, countdown_day_name, countdown_day_target_year,
                                               countdown_day_target_month,
                                               countdown_day_target_day)
        print('test_edit_a_countdown_day_with_input1 ok')

    def test_edit_a_countdown_day_with_input2(self):
        # create a_countdown_day
        click_create_countdown_day_button(self)
        # 輸入到數日名稱
        countdown_day_name = '中文倒數日'
        input_countdown_day_name(self, countdown_day_name)
        # 保存
        click_save_button(self)

        # edit
        read_countdown_day(self, countdown_day_name)
        click_edit_button(self)

        countdown_day_target_year = 2021
        countdown_day_target_month = 7
        countdown_day_target_day = 10
        countdown_day_countdown_book = '工作'
        countdown_day_repeat = 'Months'

        set_countdown_day_target_day(self, countdown_day_target_year, countdown_day_target_month,
                                     countdown_day_target_day)
        set_countdown_day_countdown_book(self, countdown_day_countdown_book)
        # click_countdown_day_set_top_button(self)
        set_countdown_day_repeat(self, countdown_day_repeat)
        # 保存
        click_save_button(self)

        verify_edit_countdown_day_successfully(self, countdown_day_name, countdown_day_target_year,
                                               countdown_day_target_month,
                                               countdown_day_target_day)
        print('test_edit_a_countdown_day_with_input2 ok')

    def test_edit_a_countdown_day_with_input3(self):
        # create a_countdown_day
        click_create_countdown_day_button(self)
        # 輸入到數日名稱
        countdown_day_name = 'ea'
        input_countdown_day_name(self, countdown_day_name)
        # 保存
        click_save_button(self)

        # edit
        read_countdown_day(self, countdown_day_name)
        click_edit_button(self)

        countdown_day_target_year = 2022
        countdown_day_target_month = 6
        countdown_day_target_day = 9
        countdown_day_countdown_book = '工作'
        countdown_day_repeat = 'Months'

        set_countdown_day_target_day(self, countdown_day_target_year, countdown_day_target_month,
                                     countdown_day_target_day)
        set_countdown_day_countdown_book(self, countdown_day_countdown_book)
        click_countdown_day_set_top_button(self)
        # set_countdown_day_repeat(self, countdown_day_repeat)
        # 保存
        click_save_button(self)
        verify_edit_countdown_day_successfully(self, countdown_day_name, countdown_day_target_year,
                                               countdown_day_target_month,
                                               countdown_day_target_day)
        print("test_edit_a_countdown_day_with_input3 ok")

    def tearDown(self) -> None:
        self.driver.quit()
