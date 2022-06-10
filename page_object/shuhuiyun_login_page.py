# encoding: utf-8
"""
@author: leeplee
@email:laputalsy@163.com
"""
from selenium import webdriver

from page.webpage import WebPage, sleep
from common.readelement import Element
import ddddocr


class SHYLoginPage(WebPage):
    """登录页类"""

    def __init__(self, driver):
        super().__init__(driver)
        self.login = Element('shuhuiyun_login')

    def input_username(self, content):
        """输入用户名"""
        self.input_text(self.login['输入用户名'], txt=content, timeout=20)
        sleep()

    def input_password(self, content):
        """输入密码"""
        self.input_text(self.login['输入密码'], txt=content, timeout=20)
        sleep()

    def input_captcha(self):
        """输入验证码"""
        sleep(2)
        self.is_click(self.login['验证码图片'], timeout=20)
        sleep(2)
        ele = self.find_element(self.login['验证码图片'], timeout=20)  # 定位验证码图片
        ele.screenshot('D:\project_auto\Autotest_ui\screen_capture\login.png')  # 截取验证码保存
        ocr = ddddocr.DdddOcr()
        with open('D:\project_auto\Autotest_ui\screen_capture\login.png', 'rb') as f:
            img = f.read()
        result = ocr.classification(img)
        print(result)

        self.input_text(self.login['输入验证码'], txt=result, timeout=20)
        sleep()

    def click_login(self):
        """点击登录"""
        self.is_click(self.login['登录按钮'], timeout=20)
        sleep()


if __name__ == '__main__':
    l = SHYLoginPage(webdriver.Chrome())
    print(l.login['输入用户名'])
