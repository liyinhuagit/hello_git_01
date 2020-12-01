from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ResPage(BaseAction):
    title_lable=By.ID,"com.android.contacts:id/large_title"

    def get_title_edit(self):
        return self.get_text(self.title_lable)
