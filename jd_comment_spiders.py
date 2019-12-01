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

import csv
import datetime
import sys


import pymongo

import requests, json
import datetime
import pandas as pd
import time
client = pymongo.MongoClient(host='120.78.155.43', port=27017)
mydb = client["jd"]
mycol = mydb["sites"]
def get_ajax(url,page_url):
    headers = {
        'referer': page_url,  # referer: https://item.jd.com/3756271.html
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    return json.loads(response.text[26:-2])


def make_url(baseurl, page=0, score=0, productId='3756271'):
    data1 = {
        'callback': 'fetchJSON_comment98vv7490',
        'productId': productId,
        'score': score,
        'sortType': '6',
        'page': page,
        'pageSize': '10',
        'isShadowSku': '0',  #
        'fold': '1',  #
    }
    url = baseurl + urlencode(data1)
    return url


def parse_json(rjson, url=None,SKU_ID=None):
    for comment in rjson.get('comments'):
        item = {}
        item['url'] = url
        item['评论星级'] = comment.get('score')
        item['评论长度'] = len(comment.get('content'))
        item['评论点赞数量'] = comment.get('usefulVoteCount')
        item['评论回复数量'] = comment.get('replyCount')
        item['评论文本内容'] = comment.get('content')
        item['评论者等级'] = comment.get('userLevelId')
        item['SKU_ID'] = SKU_ID
        try:
            date1 = time.strptime(comment.get('creationTime'), "%Y-%m-%d %H:%M:%S")
            # date2 = time.localtime(time.time())
            date1 = datetime.datetime(date1[0], date1[1], date1[2])
            # date2 = datetime.datetime(date2[0], date2[1], date2[2])
            item['评论发表时间'] = str(date1)
        except Exception as error:
            print('error is >>>', error)
            item['评论发表距抓取的天数（days）'] = ''
        if comment.get('afterUserComment', {}).get('hAfterUserComment', {}).get('content', '') == '此用户未填写评价内容':
            item['追评文本内容'] = ''
        else:
            item['追评文本内容'] = comment.get('afterUserComment', {}).get('hAfterUserComment', {}).get('content', '')
        try:
            date2 = time.strptime(comment.get('afterUserComment', {}).get('created', ''), "%Y-%m-%d %H:%M:%S")
            # print("date2",date2)
            # date2 = time.localtime(time.time())
            date2 = datetime.datetime(date2[0], date2[1], date2[2])
            # date2 = datetime.datetime(date2[0], date2[1], date2[2])
            # item['追评与初评相距时间'] = str((date2 - date1).days)
            item['追评发表的时间'] =str(date2)
        except Exception:
            # item['追评与初评相距时间'] = ''
            item['追评发表的时间'] =''
        if item['追评文本内容'] == '':
            # item['追评与初评相距时间'] = ''
            item['追评发表的时间'] =''
        yield item




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



def crawl_all_page_url():
    global ALL_PAGE_URL
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 20)

    browser.get('https://www.jd.com/allSort.aspx')
    wait.until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[5]/div[2]/div[1]/div[2]/div[2]/div[9]/div[2]/div[3]')))

    CASE = []
    for i in range(10):  # 水果
        initcase = '/html/body/div[5]/div[2]/div[1]/div[2]/div[2]/div[9]/div[2]/div[3]/dl[2]/dd/a[{}]'.format(i + 1)
        CASE.append(initcase)
    for i in range(4):  # 猪肉羊肉
        initcase = '/html/body/div[5]/div[2]/div[1]/div[2]/div[2]/div[9]/div[2]/div[3]/dl[3]/dd/a[{}]'.format(i + 1)
        CASE.append(initcase)
    for i in range(8):  # 海鲜水产
        initcase = '/html/body/div[5]/div[2]/div[1]/div[2]/div[2]/div[9]/div[2]/div[3]/dl[4]/dd/a[{}]'.format(i + 1)
        CASE.append(initcase)
    for i in range(4):  # 禽肉蛋白
        initcase = '/html/body/div[5]/div[2]/div[1]/div[2]/div[2]/div[9]/div[2]/div[3]/dl[5]/dd/a[{}]'.format(i + 1)
        CASE.append(initcase)
    for i in range(6):  # 冷冻食品
        initcase = '/html/body/div[5]/div[2]/div[1]/div[2]/div[2]/div[9]/div[2]/div[3]/dl[6]/dd/a[{}]'.format(i + 1)
        CASE.append(initcase)
    # 规则只要更改range里面的值和dl[]里面的值，可高度扩展

    for case in CASE:
        print('>>>>>>>>>')
        submit = wait.until(EC.element_to_be_clickable(
            (By.XPATH, case)))
        submit.click()

        print(browser.current_url)

        handle = browser.current_window_handle
        handles = browser.window_handles
        for newhandle in handles:
            if newhandle != handle:
                browser.switch_to.window(newhandle)
        time.sleep(1.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="plist"]/ul[contains(@class,"gl-warp")]')))
        doc = pq(browser.page_source, parser='html')
        for li in list(doc('div#plist ul.gl-warp li').items())[:10]:
            res = 'https:' + str(li('div div.p-commit-n strong a').attr('href')).replace('#comment', '')
            print(res)
            ALL_PAGE_URL.append(res)
        time.sleep(1.5)
        browser.close()
        browser.switch_to.window(handle)



if __name__ == '__main__':
    # 前期准备>>>>>>>>>>
    browser = webdriver.Chrome(executable_path='D:/chromedriver.exe')  # selenium模拟浏览器
    # driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')
    wait = WebDriverWait(browser, 20)
    MAXINDEX = 35  # 最大请求评论页数,为了控制评论数量在500条左右，应该设置为35左右，35时略大于500(网页评论非无限下拉)

    # 用户自定义配置区********************************
    TIMESLEEP = 2  # 睡眠间隔
    start = time.time()

    ALL_PAGE_URL=list(pd.read_excel("GiftGoodsInfo.xls")["skuId"])

    # num=ALL_PAGE_URL.index(21399667833)
    # print(num)
    # exit()
    #100004573430      求index
    for SKU_ID in ALL_PAGE_URL[445:]:
            page_url="https://item.jd.com/"+str(SKU_ID)+".html"
            try:
                # html = get_page(page_url)  # 请求网页，selenium动态渲染
                Flag = 1  # 计数器
                ITEMS = []
                baseurl = 'https://sclub.jd.com/comment/productPageComments.action?'
                for score in [5, 3, 2, 1]:  # 0全部评论，5追评，3好评，2中评，1差评
                    if score == 5:
                        MAXINDEX_TEMP = MAXINDEX
                    else:
                        MAXINDEX_TEMP = int(MAXINDEX / 7)  # 控制比例为7：1：1：1

                    for index in range(MAXINDEX_TEMP):
                        time.sleep(TIMESLEEP)
                        url = make_url(baseurl, page=index, score=score,
                                       productId=''.join(list(filter(str.isdigit, page_url))))  # 构造url
                        try:
                            json_ = get_ajax(url,page_url)  # 进行ajax请求
                            if len(json_.get('comments')) != 0:
                                for item in parse_json(json_, page_url,SKU_ID):  # 解析json
                                    try:
                                        # pass
                                        mycol.insert_one(item)
                                        cpprint(item)
                                        Flag+=1
                                    except Exception as error:
                                        print(error)


                            else:
                                break
                        except Exception as error:
                            if Flag!=0:
                                Flag=0
                                print('AJAX请求发生错误{}>>>'.format(error))
                                print(SKU_ID)
                                print('url is {}'.format(url))
                                print(str(datetime.datetime.now()))
                                time.sleep( 60*60*0.5 )#如何被封就暂停1h 再接着爬
                            else:
                                print('AJAX请求发生错误{}>>>'.format(error))
                                print(SKU_ID)
                                print('url is {}'.format(url))
                                print(str(datetime.datetime.now()))
                                sys.exit(0)  # ajax请求出错时退出程序，确保数据完整性
            except Exception as error:
                print(SKU_ID)
                print('网页请求发生错误{}>>>'.format(error))

        # print('一个网页请求已经结束>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # time.sleep(TIMESLEEP)

    end = time.time()
    print('总共用时{}秒'.format(end - start))