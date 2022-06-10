# encoding: utf-8
"""
@author: leeplee
@email:laputalsy@163.com
"""
from common.readelement import Element
from page.webpage import WebPage


class AIHomePage(WebPage):
    """AI主页"""
    def __init__(self, driver):
        super().__init__(driver)
        self.AI_home = Element('AI_home')

    def to_dataset(self):
        """跳转数据集管理"""
        self.is_click(locator=self.AI_home['数据集管理'], timeout=20)

    pass
