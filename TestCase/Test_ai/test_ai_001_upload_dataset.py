# encoding: utf-8
"""
@author: leeplee
@email:laputalsy@163.com
"""
import pytest
import allure
from page_object.AI_dataset_page import AIDatasetPage
from page_object.AI_home_page import AIHomePage
from common.readconfig import ini
from utils.times import sleep


@allure.feature("测试AI上传源数据集")
class TestAIUploadDataset:
    @pytest.fixture(scope='function', autouse=True)
    def open_aihome(self, drivers):
        # 打开在线训练主页
        home = AIHomePage(drivers)
        home.get_url(ini.ai_url)

    @allure.story("正向上传源数据集用例")
    def test_001(self, drivers):
        # 建立相关页面对象
        home = AIHomePage(drivers)
        dataset = AIDatasetPage(drivers)
        # 跳转数据集管理
        home.to_dataset()
        sleep()
        dataset.to_contents_dataset()
        dataset.upload_dataset('GF1B_PMS_E86.4_N44.1_20200728_L3B1227844034.zip')
        x = dataset.label_alignment()
        y = dataset.create_dataset(x)
        sleep()
        dataset.refresh()
        # 找到源数据集列表第一行数据名称的页面对象
        name = dataset.find_datasetname1()
        assert y in name.text

    def test_002(self, drivers):
        # 建立相关页面对象
        home = AIHomePage(drivers)
        dataset = AIDatasetPage(drivers)
        # 跳转数据集管理
        home.to_dataset()
        sleep()
        dataset.to_contents_dataset()
        dataset.upload_dataset('GF1_PMS1_E120.7_N28.9_20201110_L3B0005180315.zip')
        x = dataset.label_alignment()
        y = dataset.create_dataset(x)
        sleep()
        dataset.refresh()
        # 找到源数据集列表第一行数据名称的页面对象
        name = dataset.find_datasetname1()
        assert y in name.text

    def test_003(self, drivers):
        # 建立相关页面对象
        home = AIHomePage(drivers)
        dataset = AIDatasetPage(drivers)
        # 跳转数据集管理
        home.to_dataset()
        sleep()
        dataset.to_contents_dataset()
        dataset.upload_dataset('GF2_PMS1_E120.3_N30.3_20210323_L3B0005550082.zip')
        x = dataset.label_alignment()
        y = dataset.create_dataset(x)
        sleep()
        dataset.refresh()
        # 找到源数据集列表第一行数据名称的页面对象
        name = dataset.find_datasetname1()
        assert y in name.text

if __name__ == '__main__':
    pytest.main(['TestCase/Test_ai/test_ai_001_upload_dataset.py'])