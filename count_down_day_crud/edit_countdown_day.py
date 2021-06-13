import time
import unittest

from count_down_day_crud.create_countdown_day import skip_how_to_use, click_create_countdown_day_button, \
    input_countdown_day_name, set_countdown_day_target_day, set_countdown_day_countdown_book, set_countdown_day_repeat, \
    click_save_button, click_countdown_day_set_top_button, get_date_of_before, click_back_button, click_blank_space, \
    click_set_countdown_book_button
from count_down_day_crud.read_countdown_day import read_countdown_day
from keywords.open import appium_start_Session


def click_edit_button(self):
    self.driver.find_element_by_xpath('//android.widget.TextView[@content-desc="編輯"]').click()


def clear_countdown_day_name(self):
    self.driver.find_element_by_id("com.clover.daysmatter:id/text_title").clear()


def edit_countdown_day_name(self, countdown_day_name):
    clear_countdown_day_name(self)
    input_countdown_day_name(self, countdown_day_name)


def set_countdown_day_top(self):
    click_countdown_day_set_top_button(self)


def verify_edit_countdown_day_name_successfully(self, countdown_day_name):
    assert countdown_day_name in self.driver.find_element_by_id("com.clover.daysmatter:id/text_title").get_attribute(
        'name')


def verify_edit_countdown_day_target_day_successfully(self, countdown_day_target_year, countdown_day_target_month,
                                                      countdown_day_target_day):
    assert str(countdown_day_target_year) in self.driver.find_element_by_xpath(
        '//*[@resource-id="com.clover.daysmatter:id/text_due_date"]').get_attribute('name')
    assert str(countdown_day_target_month) in self.driver.find_element_by_xpath(
        '//*[@resource-id="com.clover.daysmatter:id/text_due_date"]').get_attribute('name')
    assert str(countdown_day_target_day) in self.driver.find_element_by_xpath(
        '//*[@resource-id="com.clover.daysmatter:id/text_due_date"]').get_attribute('name')


def verify_edit_countdown_day_countdown_book_successfully(self, countdown_day_countdown_book):
    assert countdown_day_countdown_book in self.driver.find_element_by_id(
        "com.clover.daysmatter:id/summary_category").get_attribute('name')


def verify_edit_countdown_day_top_successfully(self, countdown_day_name):
    assert countdown_day_name in self.driver.find_element_by_xpath(
        '//*[@resource-id="com.clover.daysmatter:id/date_big_title"]').get_attribute('name')


def verify_edit_countdown_day_repeat_successfully(self, countdown_day_repeat):
    countdown_day_repeat_str = ''
    if countdown_day_repeat == 'Weeks':
        countdown_day_repeat_str = '每週重複'
    elif countdown_day_repeat == 'Months':
        countdown_day_repeat_str = '每月重複'
    assert countdown_day_repeat_str in self.driver.find_element_by_id(
        "com.clover.daysmatter:id/summary_repeat").get_attribute('name')


def create_countdown_day_countdown_book(self, countdown_day_countdown_book):
    self.driver.find_element_by_xpath('//*[contains(@text, "添加新倒數本")]').click()
    self.driver.find_element_by_id('com.clover.daysmatter:id/text_title').send_keys(countdown_day_countdown_book)
    self.driver.find_element_by_id('com.clover.daysmatter:id/button_save').click()


class TestCountdownDayEdit(unittest.TestCase):
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

        read_countdown_day(self, self.countdown_day_name)

    def test_edit_a_countdown_day_with_input1(self):
        countdown_day_name = 'english_countdown_name'
        target_date_list = get_date_of_before(0)  # 今天
        countdown_day_target_year = int(target_date_list[0])
        countdown_day_target_month = int(target_date_list[1])
        countdown_day_target_day = int(target_date_list[2])
        countdown_day_countdown_book = '工作'
        countdown_day_repeat = 'Weeks'

        click_edit_button(self)
        edit_countdown_day_name(self, countdown_day_name)
        set_countdown_day_target_day(self,
                                     countdown_day_target_year,
                                     countdown_day_target_month,
                                     countdown_day_target_day)
        set_countdown_day_countdown_book(self, countdown_day_countdown_book)
        set_countdown_day_top(self)
        set_countdown_day_repeat(self, countdown_day_repeat)
        # 保存
        click_save_button(self)
        # verify top
        click_back_button(self)
        verify_edit_countdown_day_top_successfully(self, countdown_day_name)
        click_blank_space(self)
        read_countdown_day(self, countdown_day_name)
        click_edit_button(self)
        verify_edit_countdown_day_name_successfully(self, countdown_day_name)
        verify_edit_countdown_day_target_day_successfully(self,
                                                          countdown_day_target_year,
                                                          countdown_day_target_month,
                                                          countdown_day_target_day)
        verify_edit_countdown_day_countdown_book_successfully(self, countdown_day_countdown_book)
        verify_edit_countdown_day_repeat_successfully(self, countdown_day_repeat)
        print('test_edit_a_countdown_day_with_input1 ok')

    def test_edit_a_countdown_day_with_input2(self):
        countdown_day_name = '中文倒數日'
        target_date_list = get_date_of_before(365)  # 今天之前
        countdown_day_target_year = int(target_date_list[0])
        countdown_day_target_month = int(target_date_list[1])
        countdown_day_target_day = int(target_date_list[2])
        countdown_day_countdown_book = '新增的倒數本'
        countdown_day_repeat = 'Weeks'

        click_edit_button(self)
        edit_countdown_day_name(self, countdown_day_name)
        set_countdown_day_target_day(self,
                                     countdown_day_target_year,
                                     countdown_day_target_month,
                                     countdown_day_target_day)
        click_set_countdown_book_button(self)
        create_countdown_day_countdown_book(self, countdown_day_countdown_book)
        self.driver.find_element_by_xpath(
            '//*[@class="android.widget.TextView" and @resource-id="com.clover.daysmatter:id/list_item_title" and @text=' + '\"' + countdown_day_countdown_book + '\"' + ']').click()
        set_countdown_day_repeat(self, countdown_day_repeat)
        # 保存
        click_save_button(self)
        click_edit_button(self)
        verify_edit_countdown_day_name_successfully(self, countdown_day_name)
        verify_edit_countdown_day_countdown_book_successfully(self, countdown_day_countdown_book)
        verify_edit_countdown_day_target_day_successfully(self,
                                                          countdown_day_target_year,
                                                          countdown_day_target_month,
                                                          countdown_day_target_day)
        verify_edit_countdown_day_repeat_successfully(self, countdown_day_repeat)
        print('test_edit_a_countdown_day_with_input2 ok')

    def test_edit_a_countdown_day_with_input3(self):
        countdown_day_name = '中文倒數日'
        target_date_list = get_date_of_before(-365)  #
        countdown_day_target_year = int(target_date_list[0])
        countdown_day_target_month = int(target_date_list[1])
        countdown_day_target_day = int(target_date_list[2])
        countdown_day_countdown_book = '工作'
        countdown_day_repeat = 'Months'

        click_edit_button(self)
        edit_countdown_day_name(self, countdown_day_name)
        set_countdown_day_target_day(self,
                                     countdown_day_target_year,
                                     countdown_day_target_month,
                                     countdown_day_target_day)
        set_countdown_day_countdown_book(self, countdown_day_countdown_book)
        set_countdown_day_repeat(self, countdown_day_repeat)
        # 保存
        click_save_button(self)
        click_edit_button(self)
        verify_edit_countdown_day_name_successfully(self, countdown_day_name)
        verify_edit_countdown_day_countdown_book_successfully(self, countdown_day_countdown_book)
        verify_edit_countdown_day_target_day_successfully(self,
                                                          countdown_day_target_year,
                                                          countdown_day_target_month,
                                                          countdown_day_target_day)
        verify_edit_countdown_day_repeat_successfully(self, countdown_day_repeat)
        print('test_edit_a_countdown_day_with_input3 ok')

    def test_edit_a_countdown_day_with_input4(self):
        countdown_day_name = 'english_countdown_name'
        target_date_list = get_date_of_before(-365)  # 今天之後
        countdown_day_target_year = int(target_date_list[0])
        countdown_day_target_month = int(target_date_list[1])
        countdown_day_target_day = int(target_date_list[2])
        countdown_day_countdown_book = '新增的倒數本'

        click_edit_button(self)
        edit_countdown_day_name(self, countdown_day_name)
        set_countdown_day_target_day(self,
                                     countdown_day_target_year,
                                     countdown_day_target_month,
                                     countdown_day_target_day)
        click_set_countdown_book_button(self)
        create_countdown_day_countdown_book(self, countdown_day_countdown_book)
        self.driver.find_element_by_xpath(
            '//*[@class="android.widget.TextView" and @resource-id="com.clover.daysmatter:id/list_item_title" and @text=' + '\"' + countdown_day_countdown_book + '\"' + ']').click()
        set_countdown_day_top(self)
        # 保存
        click_save_button(self)
        click_edit_button(self)
        verify_edit_countdown_day_name_successfully(self, countdown_day_name)
        verify_edit_countdown_day_target_day_successfully(self,
                                                          countdown_day_target_year,
                                                          countdown_day_target_month,
                                                          countdown_day_target_day)
        verify_edit_countdown_day_countdown_book_successfully(self, countdown_day_countdown_book)
        print('test_edit_a_countdown_day_with_input4 ok')

    def test_edit_a_countdown_day_with_input5(self):
        countdown_day_name = 'english_countdown_name'
        target_date_list = get_date_of_before(365)  # 今天
        countdown_day_target_year = int(target_date_list[0])
        countdown_day_target_month = int(target_date_list[1])
        countdown_day_target_day = int(target_date_list[2])
        countdown_day_countdown_book = '工作'
        countdown_day_repeat = 'Months'

        click_edit_button(self)
        edit_countdown_day_name(self, countdown_day_name)
        set_countdown_day_target_day(self,
                                     countdown_day_target_year,
                                     countdown_day_target_month,
                                     countdown_day_target_day)
        set_countdown_day_countdown_book(self, countdown_day_countdown_book)
        set_countdown_day_top(self)
        set_countdown_day_repeat(self, countdown_day_repeat)
        # 保存
        click_save_button(self)
        click_edit_button(self)
        verify_edit_countdown_day_name_successfully(self, countdown_day_name)
        verify_edit_countdown_day_target_day_successfully(self,
                                                          countdown_day_target_year,
                                                          countdown_day_target_month,
                                                          countdown_day_target_day)
        verify_edit_countdown_day_countdown_book_successfully(self, countdown_day_countdown_book)
        verify_edit_countdown_day_repeat_successfully(self, countdown_day_repeat)
        print('test_edit_a_countdown_day_with_input5 ok')

    def test_edit_a_countdown_day_with_input6(self):
        countdown_day_name = '中文倒數日'
        target_date_list = get_date_of_before(0)  # 今天
        countdown_day_target_year = int(target_date_list[0])
        countdown_day_target_month = int(target_date_list[1])
        countdown_day_target_day = int(target_date_list[2])
        countdown_day_countdown_book = '新增的倒數本'
        countdown_day_repeat = 'Weeks'

        click_edit_button(self)
        edit_countdown_day_name(self, countdown_day_name)
        set_countdown_day_target_day(self,
                                     countdown_day_target_year,
                                     countdown_day_target_month,
                                     countdown_day_target_day)
        click_set_countdown_book_button(self)
        create_countdown_day_countdown_book(self, countdown_day_countdown_book)
        self.driver.find_element_by_xpath(
            '//*[@class="android.widget.TextView" and @resource-id="com.clover.daysmatter:id/list_item_title" and @text=' + '\"' + countdown_day_countdown_book + '\"' + ']').click()
        set_countdown_day_top(self)
        set_countdown_day_repeat(self, countdown_day_repeat)
        # 保存
        click_save_button(self)
        click_edit_button(self)
        verify_edit_countdown_day_name_successfully(self, countdown_day_name)
        verify_edit_countdown_day_target_day_successfully(self,
                                                          countdown_day_target_year,
                                                          countdown_day_target_month,
                                                          countdown_day_target_day)
        verify_edit_countdown_day_countdown_book_successfully(self, countdown_day_countdown_book)
        verify_edit_countdown_day_repeat_successfully(self, countdown_day_repeat)
        print('test_edit_a_countdown_day_with_input6 ok')

    def test_edit_a_countdown_day_with_input7(self):
        countdown_day_name = '中文倒數日'
        target_date_list = get_date_of_before(0)  # 今天
        countdown_day_target_year = int(target_date_list[0])
        countdown_day_target_month = int(target_date_list[1])
        countdown_day_target_day = int(target_date_list[2])
        countdown_day_countdown_book = '新增的倒數本'
        countdown_day_repeat = 'Months'

        click_edit_button(self)
        edit_countdown_day_name(self, countdown_day_name)
        set_countdown_day_target_day(self,
                                     countdown_day_target_year,
                                     countdown_day_target_month,
                                     countdown_day_target_day)
        click_set_countdown_book_button(self)
        create_countdown_day_countdown_book(self, countdown_day_countdown_book)
        self.driver.find_element_by_xpath(
            '//*[@class="android.widget.TextView" and @resource-id="com.clover.daysmatter:id/list_item_title" and @text=' + '\"' + countdown_day_countdown_book + '\"' + ']').click()
        set_countdown_day_repeat(self, countdown_day_repeat)
        # 保存
        click_save_button(self)
        click_edit_button(self)
        verify_edit_countdown_day_name_successfully(self, countdown_day_name)
        verify_edit_countdown_day_target_day_successfully(self,
                                                          countdown_day_target_year,
                                                          countdown_day_target_month,
                                                          countdown_day_target_day)
        verify_edit_countdown_day_countdown_book_successfully(self, countdown_day_countdown_book)
        verify_edit_countdown_day_repeat_successfully(self, countdown_day_repeat)
        print('test_edit_a_countdown_day_with_input7 ok')

    def test_edit_a_countdown_day_with_input8(self):
        countdown_day_name = 'english_countdown_name'
        target_date_list = get_date_of_before(365)  # 今天之前
        countdown_day_target_year = int(target_date_list[0])
        countdown_day_target_month = int(target_date_list[1])
        countdown_day_target_day = int(target_date_list[2])
        countdown_day_countdown_book = '工作'

        click_edit_button(self)
        edit_countdown_day_name(self, countdown_day_name)
        set_countdown_day_target_day(self,
                                     countdown_day_target_year,
                                     countdown_day_target_month,
                                     countdown_day_target_day)
        set_countdown_day_countdown_book(self, countdown_day_countdown_book)
        # 保存
        click_save_button(self)
        click_edit_button(self)
        verify_edit_countdown_day_name_successfully(self, countdown_day_name)
        verify_edit_countdown_day_target_day_successfully(self,
                                                          countdown_day_target_year,
                                                          countdown_day_target_month,
                                                          countdown_day_target_day)
        verify_edit_countdown_day_countdown_book_successfully(self, countdown_day_countdown_book)
        print('test_edit_a_countdown_day_with_input8 ok')

    def test_edit_a_countdown_day_with_input9(self):
        countdown_day_name = 'english_countdown_name'
        target_date_list = get_date_of_before(-365)  # 今天之後
        countdown_day_target_year = int(target_date_list[0])
        countdown_day_target_month = int(target_date_list[1])
        countdown_day_target_day = int(target_date_list[2])
        countdown_day_countdown_book = '工作'
        countdown_day_repeat = 'Weeks'

        click_edit_button(self)
        edit_countdown_day_name(self, countdown_day_name)
        set_countdown_day_target_day(self,
                                     countdown_day_target_year,
                                     countdown_day_target_month,
                                     countdown_day_target_day)
        set_countdown_day_countdown_book(self, countdown_day_countdown_book)
        set_countdown_day_repeat(self, countdown_day_repeat)
        # 保存
        click_save_button(self)
        click_edit_button(self)
        verify_edit_countdown_day_name_successfully(self, countdown_day_name)
        verify_edit_countdown_day_target_day_successfully(self,
                                                          countdown_day_target_year,
                                                          countdown_day_target_month,
                                                          countdown_day_target_day)
        verify_edit_countdown_day_countdown_book_successfully(self, countdown_day_countdown_book)
        verify_edit_countdown_day_repeat_successfully(self, countdown_day_repeat)
        print('test_edit_a_countdown_day_with_input9 ok')

    def tearDown(self) -> None:
        self.driver.quit()
