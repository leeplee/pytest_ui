# encoding: utf-8
"""
@author: leeplee
@email:laputalsy@163.com
"""
import pytest
import allure
from common.readconfig import ini
from page_object.AI_dataset_page import AIDatasetPage
from page_object.AI_home_page import AIHomePage
from utils.times import sleep


@allure.feature("测试AI细化标签发起")
class TestAIFeatureCalculate:
    @pytest.fixture(scope='function', autouse=True)
    def open_aihome(self, drivers):
        # 打开在线训练主页
        home = AIHomePage(drivers)
        home.get_url(ini.ai_url)

    @allure.story("正向发起细化标签用例")
    def test_001(self, drivers):
        # 建立相关页面对象
        home = AIHomePage(drivers)
        dataset = AIDatasetPage(drivers)
        # 跳转数据集管理
        home.to_dataset()
        sleep()
        dataset.to_contents_dataset()
        x = dataset.create_refine_label().text
        dataset.refresh()
        y = dataset.find_refinelabelname1().text
        assert x in y


if __name__ == '__main__':
    pytest.main(['TestCase/Test_ai/test_ai_003_refine_label.py'])
