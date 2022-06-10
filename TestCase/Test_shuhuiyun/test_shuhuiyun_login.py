#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pytest
import allure
from utils.logger import log
from common.readconfig import ini
from page_object.shuhuiyun_home_page import SHYHomePage
from page_object.shuhuiyun_login_page import SHYLoginPage
from utils.times import sleep


@allure.feature("测试主页登录模块")
class TestLogin:
    @pytest.fixture(scope='function', autouse=True)
    def open_shuhuiyun(self, drivers):
        """打开数慧云"""
        home = SHYHomePage(drivers)
        home.get_url(ini.home_url)

    @allure.story("正向登录用例")
    def test_001(self, drivers):
        """正向登录"""
        # 建立相关的页面对象
        home = SHYHomePage(drivers)
        login = SHYLoginPage(drivers)
        # 以下是流程
        home.click_login()
        sleep()
        login.input_username('admin')
        login.input_password('qwert1234')
        login.input_captcha()
        login.click_login()
        log.info(home.find_login())
        assert home.find_login() == 'admin'


if __name__ == '__main__':
    pytest.main(['TestCase/Test_shuhuiyun/test_shuhuiyun_login.py'])
