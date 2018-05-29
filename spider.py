#!/usr/bin/env python3
# coding: utf-8
# File: spider.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-5-29
# 功能: 指定商品名称，获取器阿里指数，只能抓取一年。

from selenium import webdriver
from lxml import etree
import json
import datetime
import os

class AliIndex:
    def __init__(self):
        self.index_page = 'https://index.1688.com/alizs/market.htm'
    '''搜索指数入口'''
    def search_index(self, search_word):
        driver = webdriver.Firefox()
        driver.get(self.index_page)
        e1 = driver.find_element_by_id('alizs-input')
        e1.send_keys(search_word)
        e2 = driver.find_element_by_id('alizs-submit')
        e2.click()
        page_source = driver.page_source
        import time
        time.sleep(200)
        driver.close()
        return page_source

    '''数据解析'''
    def data_parser(self, content):
        selector = etree.HTML(content)
        data = json.loads(selector.xpath('//input[@id="main-chart-val"]/@value')[0])
        purchaseIndex1688 = data['purchaseIndex1688']['index']['history']
        supplyIndex = data['supplyIndex']['index']['history']
        purchaseIndexTb = data['purchaseIndexTb']['index']['history']
        today = datetime.date.today()
        date_list = [(today - datetime.timedelta(days=num)).strftime('%Y-%m-%d') for num in range(366, 0, -1)]
        purchase_index_1688 = zip(date_list, purchaseIndex1688)
        supply_index = zip(date_list, supplyIndex)
        purchase_index_tb = zip(date_list, purchaseIndexTb)
        return purchase_index_1688, supply_index, purchase_index_tb

    '''以写入本地文件的方式，保存数据'''
    def write_localfiles(self, word, data, filepath):
        if not os.path.exists(word):
            os.makedirs(word)
        with open(filepath, 'w+') as f:
            for item in data:
                f.write(item[0] + ',' + str(item[1]) + "\n")
        f.close()

    '''导出数据'''
    def output_data(self, word, purchase_index_1688, supply_index, purchase_index_tb):
        self.write_localfiles(word, purchase_index_1688, '%s/%s.txt'%(word, 'purchase_index_1688'))
        self.write_localfiles(word, supply_index, '%s/%s.txt' % (word, 'supply_index'))
        self.write_localfiles(word, purchase_index_tb, '%s/%s.txt' % (word, 'purchase_index_tb'))

    '''主函数'''
    def index_main(self, word):
        print('step1, open page....')
        page_source = self.search_index(word)
        print('step2, get data....')
        purchase_index_1688, supply_index, purchase_index_tb = self.data_parser(page_source)
        self.output_data(word, purchase_index_1688, supply_index, purchase_index_tb)
        print('step3, %s finished....'% word)

def demo():
    ali = AliIndex()
    search_word = '连衣裙'
    ali.index_main(search_word)

demo()