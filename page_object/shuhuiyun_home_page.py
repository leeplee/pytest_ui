#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from selenium import webdriver
from page.webpage import WebPage, sleep
from common.readelement import Element


class SHYHomePage(WebPage):
    """主页类"""
    def __init__(self, driver):
        super().__init__(driver)
        self.home = Element('shuhuiyun_home')

    def click_login(self):
        """点击登录"""
        self.is_click(self.home['登录按钮'], timeout=20)

    def find_login(self):
        """找到登录成功的元素"""
        x = self.find_element(self.home['登陆成功'], timeout=20)
        return x.text


if __name__ == '__main__':
    h = SHYHomePage(webdriver.Chrome())
    print(h.home['登录按钮'])
