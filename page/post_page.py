from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class PostPage(BaseAction):
    name_label=By.XPATH,"//*[@text='姓名']"
    tel_label=By.XPATH,"//*[@text='电话']"
    sip_lable=By.XPATH,"//*[@text='sip']"
    back_lable=By.CLASS_NAME,"android.widget.ImageButton"

    def input_name_edit(self,text):

        self.input(self.name_label,text)
    def input_tel_edit(self,text):
        self.input(self.tel_label,text)

    def click_back_edit(self):
        self.click(self.back_lable)

    def  input_sip_adit(self,text):
        self.input(self.sip_lable,text)
