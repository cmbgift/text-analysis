# https://www.jd.com/allSort.aspx
import requests
from pyquery import PyQuery as pq
from prettyprinter import cpprint
import json
from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import datetime
import sys
import sql
import pandas as pd


def get_page(url):
    browser.get(url)
    submit = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"tab-main")]/ul/li[5]')))
    time.sleep(2)
    for i in range(30):
        browser.execute_script("window.scrollBy(0,50)")
        time.sleep(0.1)
    submit.click()
    time.sleep(3)
    return browser.page_source



if __name__ == '__main__':
    # 前期准备>>>>>>>>>>
    browser = webdriver.Chrome(executable_path='D:/chromedriver.exe')  # selenium模拟浏览器
    # driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')
    wait = WebDriverWait(browser, 20)
    MAXINDEX = 7  # 最大请求评论页数,为了控制评论数量在500条左右，应该设置为35左右，35时略大于500(网页评论非无限下拉)
    # 用户自定义配置区********************************

    start = time.time()
    # 爬取商品信息

    # ALL_PAGE_URL=list(pd.read_excel("GiftGoodsInfo.xls")["skuId"])
    ALL_PAGE_URL=list(pd.ExcelFile("Gift2.xlsx").parse("Sheet3")["SKU_ID"])
    # i=ALL_PAGE_URL.index(36063041972)
    # print(i)

    # exit()
    # ALL_PAGE_URL=[12707870,12707870,27026831696]
    for SKU_ID in ALL_PAGE_URL:
            try:
                page_url="https://item.jd.com/"+str(SKU_ID)+".html"
                # print(page_url)
                html = get_page(page_url)  # 请求网页，selenium动态渲染
                doc = pq(html, parser='html')
                SKU_INTRODUCE= doc('#detail > div.tab-con > div:nth-child(1)').text()
                SKU_SIZE = doc('#detail > div.tab-con > div:nth-child(2)').text()
                SKU_PRICE= doc('div.itemInfo-wrap span.p-price span.price').text()

                SKU_LABEL1= doc('#crumb-wrap > div > div.crumb.fl.clearfix > div:nth-child(1) > a').text()
                SKU_LABEL3= doc('#crumb-wrap > div > div.crumb.fl.clearfix > div:nth-child(3) > a').text()
                SKU_LABEL5= doc('#crumb-wrap > div > div.crumb.fl.clearfix > div:nth-child(5) > a').text()
                SKU_LABEL7= doc('#crumb-wrap > div > div.crumb.fl.clearfix > div:nth-child(7) > a').text()

                SKU_TITLE= doc('div.sku-name').text() #图书类的 与其他商品 html格式不一样
                SKU_COMMENT_NUMS= doc('#detail > div.tab-main.large > ul > li.current > s').text().replace('(', '').replace(
                    ')', '')
                SKU_GOOD_RATE= doc('#comment > div.mc > div.comment-info.J-comment-info > div.comment-percent > div').text()
                # print(SKU_ID,SKU_TITLE)
                sql.insert_skus(SKU_ID, SKU_INTRODUCE, SKU_SIZE, SKU_PRICE,SKU_LABEL5,SKU_TITLE,SKU_COMMENT_NUMS,SKU_GOOD_RATE)
            except Exception as error:
                print(SKU_ID,error)
                pass

    end = time.time()
    print('总共用时{}秒'.format(end - start))
