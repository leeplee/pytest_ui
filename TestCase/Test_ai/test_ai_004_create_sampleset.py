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


@allure.feature("测试AI样本集制作任务发起")
class TestAIFeatureCalculate:
    @pytest.fixture(scope='function', autouse=True)
    def open_aihome(self, drivers):
        # 打开在线训练主页
        home = AIHomePage(drivers)
        home.get_url(ini.ai_url)

    @allure.story("正向源数据集发起样本集制作用例")
    def test_001(self, drivers):
        # 建立相关页面对象
        home = AIHomePage(drivers)
        dataset = AIDatasetPage(drivers)
        # 跳转数据集管理
        home.to_dataset()
        sleep()
        dataset.to_contents_dataset()
        x = dataset.create_sampleset_dataset()
        dataset.to_contents_sampleset()
        y = dataset.find_samplesetname1().text
        assert x in y

    @allure.story("正向特征集发起样本集制作用例")
    def test_002(self, drivers):
        # 建立相关页面对象
        home = AIHomePage(drivers)
        dataset = AIDatasetPage(drivers)
        # 跳转数据集管理
        home.to_dataset()
        sleep()
        dataset.to_contents_dataset()
        x = dataset.create_sampleset_featruecalculate()
        dataset.to_contents_sampleset()
        y = dataset.find_samplesetname1().text
        assert x in y

    @allure.story("正向细化标签集发起样本集制作用例")
    def test_003(self, drivers):
        # 建立相关页面对象
        home = AIHomePage(drivers)
        dataset = AIDatasetPage(drivers)
        # 跳转数据集管理
        home.to_dataset()
        sleep()
        dataset.to_contents_dataset()
        x = dataset.create_sampleset_refinelabel()
        dataset.to_contents_sampleset()
        y = dataset.find_samplesetname1().text
        assert x in y


if __name__ == '__main__':
    pytest.main(['TestCase/Test_ai/test_ai_004_create_sampleset.py'])
