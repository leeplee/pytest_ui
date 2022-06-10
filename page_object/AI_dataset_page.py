# encoding: utf-8
"""
@author: leeplee
@email:laputalsy@163.com
"""
import pywinauto
from pywinauto.keyboard import send_keys
from selenium import webdriver

from utils.logger import log
from common.readelement import Element
from page.webpage import WebPage
from utils.times import sleep, dt_strftime


class AIDatasetPage(WebPage):
    """数据集管理"""

    def __init__(self, driver):
        super().__init__(driver)
        self.AI_dataset = Element('AI_dataset')

    def to_contents_dataset(self):
        # 页面url不同
        self.is_click(self.AI_dataset['目录源数据集'], timeout=20)

    def to_contents_sampleset(self):
        self.is_click(self.AI_dataset['目录样本集'], timeout=20)


    def upload_dataset(self, package_name):
        """上传源数据集"""
        self.is_click(self.AI_dataset['上传源数据集'], timeout=20)
        self.is_click(self.AI_dataset['上传ZIP'], timeout=20)
        self.is_click(self.AI_dataset['上传区域'], timeout=20)
        # 使用pywinauto创建一个操作桌面窗口的对象
        win1 = pywinauto.Desktop()
        # 选择文件上传的窗口 窗口句柄默认为‘打开’
        bow1 = win1['打开']  # 火狐为 '文件上传'
        # 选择文件地址输入框，点击激活
        bow1["Toolbar3"].click()
        # 键盘输入上传文件的路径
        send_keys(r"C:\Users\bjsh\Desktop\在线训练测试数据")
        # 键盘输入回车，打开该路径
        send_keys('{VK_RETURN}')
        # 选中文件名输入框，输入文件名
        bow1['文件名(&N):Edit'].type_keys(package_name)
        sleep()
        # 点击打开
        # bow1['打开(&O)'].click()
        bow1['打开'].click()

        sleep(2)
        # 确定
        self.is_click(self.AI_dataset['上传确认'], timeout=20)
        sleep()
        try:
            x = self.find_element(self.AI_dataset['展示样式1'], timeout=60).text
            if '影像唯一' in x:
                log.info('上传矢量文件成功！')
                self.is_click(self.AI_dataset['下一步1'], timeout=20)
        except:
            y = self.find_element(self.AI_dataset['展示样式2'], timeout=60).text
            if '多幅影像' in y:
                log.info('上传矢量文件成功！')
                self.is_click(self.AI_dataset['请选择影像'], timeout=20)
                self.is_click(self.AI_dataset['第一幅影像span'], timeout=20)
                self.is_click(self.AI_dataset['选择影像确定'], timeout=20)
                self.is_click(self.AI_dataset['下一步1'], timeout=20)

    def label_alignment(self):
        global label
        self.is_click(self.AI_dataset['属性字段1'], timeout=20)
        self.input_text(self.AI_dataset['属性字段1'], timeout=20, txt="YBBQ")
        self.is_click(self.AI_dataset['属性字段2'], timeout=20)
        self.is_click(self.AI_dataset['分类器1'], timeout=20)
        self.is_click(self.AI_dataset['分类器2'], timeout=20)
        for i in range(5):
            self.is_click(self.AI_dataset['开启标签对齐'], timeout=20)
            if self.find_element(self.AI_dataset['标签列表'], timeout=120):
                label = self.find_element(locator=(
                'xpath', '/html/body/div[1]/div[6]/div[4]/div[3]/div[4]/div[2]/div/div[3]/table/tbody/tr/td[1]/div'),
                                          timeout=20).text
                self.is_click(self.AI_dataset['下一步2'], timeout=20)
                break

        return label

    def create_dataset(self, label):
        name = 'test' + dt_strftime("%m%d%H%M") + label
        self.input_text(self.AI_dataset['数据源名称'], timeout=20, txt=name)
        self.input_text(self.AI_dataset['上传人姓名'], timeout=20, txt='test')
        self.is_click(self.AI_dataset['开始创建'], timeout=20)
        return name

    def find_datasetname1(self):
        self.is_click(self.AI_dataset['源数据集tab'], timeout=20)
        return self.find_element(self.AI_dataset['源数据集列表名称1'], 20)

    def create_feature_calculate(self):
        self.is_click(self.AI_dataset['源数据集tab'], timeout=20)
        x = self.find_datasetname1()
        self.is_click(self.AI_dataset['源数据集列表勾选1'], timeout=20)
        self.is_click(self.AI_dataset['特征计算按钮'], timeout=20)
        self.is_click(self.AI_dataset['特征计算确定'], timeout=20)
        return x

    def find_featurecalculatename1(self):
        self.is_click(self.AI_dataset['特征tab'], timeout=20)
        return self.find_element(self.AI_dataset['特征列表名称1'], 20)

    def create_refine_label(self):
        global z
        self.is_click(self.AI_dataset['特征tab'], timeout=20)
        x = self.find_elements(('xpath',
                                '/html/body/div[1]/div[6]/div[3]/div[1]/div[2]/div/div[2]/div[2]/div[3]/div[5]/div[1]/div[3]/table/tbody/tr/td[3]/div'),
                               timeout=20)
        lis = []
        for i in x:
            lis.append(i.text)
        a = [i for i,x in enumerate(lis) if x=='建构筑物'] # 下标构成的列表
        for i in a:
            y = self.find_element(('xpath',
                                    f'/html/body/div[1]/div[6]/div[3]/div[1]/div[2]/div/div[2]/div[2]/div[3]/div[5]/div[1]/div[3]/table/tbody/tr[{i+1}]/td[11]/div'),
                                   timeout=20).text
            if y == '已处理':
                self.is_click(('xpath',
                               f'/html/body/div[1]/div[6]/div[3]/div[1]/div[2]/div/div[2]/div[2]/div[3]/div[5]/div[1]/div[3]/table/tbody/tr[{i+1}]/td[1]/div/label/span/span'),
                              timeout=20)
                z = self.find_element(('xpath',
                                       f'/html/body/div[1]/div[6]/div[3]/div[1]/div[2]/div/div[2]/div[2]/div[3]/div[5]/div[1]/div[3]/table/tbody/tr[{i+1}]/td[4]/div'),
                                      timeout=20)
                self.is_click(self.AI_dataset['标签细化按钮'], timeout=20)
                self.is_click(self.AI_dataset['标签细化确定'], timeout=20)
                break
            else:
                log.info('没有已处理的任务可以细化！')
        return z

    def find_refinelabelname1(self):
        self.is_click(self.AI_dataset['细化标签tab'], timeout=20)
        return self.find_element(self.AI_dataset['细化标签列表名称1'], 20)

    def create_sampleset_dataset(self):
        self.is_click(self.AI_dataset['源数据集tab'], timeout=20)
        z = self.find_datasetname1().text
        self.is_click(self.AI_dataset['源数据集列表勾选1'], timeout=20)
        self.is_click(self.AI_dataset['制作样本集1'], timeout=20)
        self.input_text(self.AI_dataset['输入样本集名称'], timeout=20, txt='dataset' + z)
        self.is_click(self.AI_dataset['制作样本集确定'], timeout=20)
        return 'dataset' + z

    def create_sampleset_featruecalculate(self):
        self.is_click(self.AI_dataset['特征tab'], timeout=20)
        x = self.find_elements(('xpath',
                                '/html/body/div[1]/div[6]/div[3]/div[1]/div[2]/div/div[2]/div[2]/div[3]/div[5]/div[1]/div[3]/table/tbody/tr/td[11]/div/div/span'),
                               timeout=20)
        lis = []
        for i in x:
            lis.append(i.text)
        a = [i for i, x in enumerate(lis) if x == '已处理']  # 下标构成的列表
        y = a[0] + 1
        # 勾选
        self.is_click(('xpath',
                       f'/html/body/div[1]/div[6]/div[3]/div[1]/div[2]/div/div[2]/div[2]/div[3]/div[5]/div[1]/div[3]/table/tbody/tr[{y}]/td[1]/div/label/span/span'),
                      timeout=20)
        z = self.find_element(('xpath',
                               f'/html/body/div[1]/div[6]/div[3]/div[1]/div[2]/div/div[2]/div[2]/div[3]/div[5]/div[1]/div[3]/table/tbody/tr[{y}]/td[4]/div'),
                              timeout=20).text
        self.is_click(self.AI_dataset['制作样本集2'], timeout=20)
        self.input_text(self.AI_dataset['输入样本集名称'], timeout=20, txt='featrue' + z)
        self.is_click(self.AI_dataset['制作样本集确定'], timeout=20)
        return 'featrue' + z


    def create_sampleset_refinelabel(self):
        self.is_click(self.AI_dataset['细化标签tab'], timeout=20)
        x = self.find_elements(('xpath',
                                '/html/body/div[1]/div[6]/div[3]/div[1]/div[2]/div/div[2]/div[3]/div[3]/div[5]/div[1]/div[3]/table/tbody/tr/td[11]/div/div/span'),
                               timeout=20)
        lis = []
        for i in x:
            lis.append(i.text)
        a = [i for i, x in enumerate(lis) if x == '已处理']  # 下标构成的列表
        y = a[0] + 1
        # 勾选
        self.is_click(('xpath',
                       f'/html/body/div[1]/div[6]/div[3]/div[1]/div[2]/div/div[2]/div[3]/div[3]/div[5]/div[1]/div[3]/table/tbody/tr[{y}]/td[1]/div/label/span/span'),
                      timeout=20)
        z = self.find_element(('xpath',
                               f'/html/body/div[1]/div[6]/div[3]/div[1]/div[2]/div/div[2]/div[3]/div[3]/div[5]/div[1]/div[3]/table/tbody/tr[{y}]/td[4]/div'),
                              timeout=20).text
        self.is_click(self.AI_dataset['制作样本集3'], timeout=20)
        self.input_text(self.AI_dataset['输入样本集名称'], timeout=20, txt='refine' + z)
        self.is_click(self.AI_dataset['制作样本集确定'], timeout=20)
        return 'refine' + z

    def find_samplesetname1(self):
        return self.find_element(self.AI_dataset['样本集列表名称1'], 20)










if __name__ == '__main__':
    # w = AIDatasetPage(webdriver.Chrome())
    # w.get_url('http://192.168.0.219/online-training-interpretation/#/stat')
    # w.is_click(('xpath', '/html/body/div[1]/div[5]/div[1]/div[2]/a[2]'), 20)
    # w.to_contents_dataset()
    # w.is_click(w.AI_dataset['特征tab'], timeout=20)
    # x = w.find_elements(('xpath',
    #                      '/html/body/div[1]/div[6]/div[3]/div[1]/div[2]/div/div[2]/div[2]/div[3]/div[5]/div[1]/div[3]/table/tbody/tr/td[3]/div'),
    #                     timeout=20)
    # lis = []
    # for i in x:
    #     lis.append(i.text)
    # print(lis)
    # for j in lis:
    #     if j == '建构筑物':
    #         print(lis.index(j))
    #         break

    lis = ['建构筑物', '建构筑物', '棉花', '套种', '辣椒', '红薯', '玉米', '山药', '其他药用', '花生']
    a = [i for i,x in enumerate(lis) if x=='建构筑物'] # 一行写法，enumerate()函数
    print(a)
