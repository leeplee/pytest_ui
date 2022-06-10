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


@allure.feature("测试AI特征计算发起")
class TestAIFeatureCalculate:
    @pytest.fixture(scope='function', autouse=True)
    def open_aihome(self, drivers):
        # 打开在线训练主页
        home = AIHomePage(drivers)
        home.get_url(ini.ai_url)

    @allure.story("正向发起特征计算用例")
    def test_001(self, drivers):
        # 建立相关页面对象
        home = AIHomePage(drivers)
        dataset = AIDatasetPage(drivers)
        # 跳转数据集管理
        home.to_dataset()
        sleep()
        dataset.to_contents_dataset()
        x = dataset.create_feature_calculate().text
        dataset.refresh()
        y = dataset.find_featurecalculatename1().text
        assert x in y

       


if __name__ == '__main__':
    pytest.main(['TestCase/Test_ai/test_ai_002_feature_calculate.py'])