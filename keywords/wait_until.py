def wait_until_UserGuideActivity_page_is_visible(self):
    self.driver.wait_activity(".ui.activity.UserGuideActivity", 30)


def wait_until_MainActivity_page_is_visible(self):
    self.driver.wait_activity(".ui.activity.MainActivity", 30)


def wait_until_DetailActivity_page_is_visible(self):
    self.driver.wait_activity(".ui.activity.DetailActivity", 30)


def wait_until_EditActivity_page_is_visible(self):
    self.driver.wait_activity(".ui.activity.EditActivity", 30)
