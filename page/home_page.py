from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    button_label=By.ID,"com.android.contacts:id/floating_action_button"
    alter_label=By.XPATH,"//*[@text='本地保存']"

    def click_button_edit(self):
        self.click(self.button_label)

    def click_alter_edit(self):
        self.click(self.alter_label)





