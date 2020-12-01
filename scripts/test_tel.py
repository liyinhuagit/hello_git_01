from time import sleep

from base.base_driver import init_driver
from page.home_page import HomePage
from page.post_page import PostPage
from page.res_page import ResPage


class TestTel:
    def setup(self):
        self.driver=init_driver()

        self.home_page=HomePage(self.driver)
        self.post_page=PostPage(self.driver)
        self.res_page=ResPage(self.driver)


    def deardonw(self):
       self.driver.quit()

    def test_tel_text(self):
        self.home_page.click_button_edit()
        self.home_page.click_alter_edit()
        sleep(3)
        self.post_page.input_name_edit("zhangsan")
        self.post_page.input_tel_edit("188888888")
        # while True:
        #     try:
        #         self.post_page.input_sip_adit("123456")
        #         self.post_page.click_back_edit()
        #         assert self.res_page.get_title_edit() == "zhangsan"
        #         return
        #     except:
        #         self.driver.swipe(100, 800, 100, 300, 2000)
        self.post_page.click_back_edit()
        assert self.res_page.get_title_edit() == "zhangsan"





