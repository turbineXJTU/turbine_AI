#!/usr/bin/env python
# -*- coding:utf-8 -*-
# anthor: 郑召利 time:2017/12/17


import time
import url_analyse
import translate
import write_to_file
import os




# 爬虫类
class Spider:
    def __init__(self):
        self.url_analyse = url_analyse.Url_analyse()
        self.translate = translate.Translate()
        self.write_to_file = write_to_file.Write_to_file()

    def run(self,KeyWords,Page_num):
        # url_pdf = 'https://ac.els-cdn.com/S0888327017301541/1-s2.0-S0888327017301541-main.pdf?_tid=4829e020-e631-11e7-aa90-00000aab0f6b&acdnat=1513848680_3cf6d2bb52f309f3b01b96fcefb431ee'
        # self.write_to_file.download_pdf(url_pdf,'xx.pdf')

        # 创建文件夹
        path = '.\\爬取结果\\' + KeyWords
        if not os.path.exists(path):
            os.makedirs(path)
        # 拼接网址
        KeyWords_split = KeyWords.split()
        start_url = 'http://www.sciencedirect.com/search?qs='
        for ii in range(0, len(KeyWords_split)):
            # 'http://www.sciencedirect.com/search?qs=turbine%20blade%20crack&show=25&sortBy=relevance'
            if ii == 0:
                start_url = start_url + KeyWords_split[ii]
            else:
                start_url = start_url + '%20' + KeyWords_split[ii]
        start_url = start_url + '&show=25&sortBy=relevance'
        # 分析起始搜索页面
        new_urls = self.url_analyse.analyse_SearchPage(start_url)
        count = 1
        # 创建结果文件
        filename = path + '\\' + KeyWords + '.txt'
        if count == 1 and os.path.exists(filename):
            os.remove(filename)
        # 开始爬虫
        while True:
            # 判断是否需要翻页
            if len(new_urls):
                new_url = new_urls[0]
                # 分析搜索结果中的每个文献，获得标题和摘要
                (title_en, abstract_en) = self.url_analyse.analyse_EveryPage(new_url, count)
                new_urls.remove(new_urls[0])
                # 利用百度翻译API翻译标题和摘要
                title_cn = self.translate.en2ch(title_en)
                abstract_cn = self.translate.en2ch(abstract_en)
                self.write_to_file.write_to_txt(filename,count,title_en,abstract_en,title_cn,abstract_cn,new_url)
                # 统计已处理的文献个数
                count = count + 1
            else:
                # 翻页
                print(start_url + '&offset=' + str(int(count-1)))
                new_urls = self.url_analyse.analyse_SearchPage(start_url + '&offset=' + str(int(count-1)))
            # 满足条件则跳出
            if count>Page_num:
                break











# 主程序
if __name__ == "__main__":
    # 实例化爬虫
    spider = Spider()
    # 统计程序开始的时间
    start = time.time()
    # 搜索关键词
    KeyWords = 'asymmetric rotor'
    Page_num = 5000
    print(KeyWords,Page_num)
    # # 浏览网页获得参考文献的标题及其链接
    spider.run(KeyWords, Page_num)



