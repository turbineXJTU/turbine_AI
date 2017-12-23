#conding:utf8

import hashlib
import json
import random
import urllib.request

import requests
import sys


class Translate(object):
    def __init__(self):
        self.ok = 'ok'

    # def en2ch(self, q):
    #     appid = '20171219000106286'
    #     secretKey = 'EfD5IS6JXqWFFp0ZwrI8'
    #     my_url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    #     fromLang = 'en'
    #     toLang = 'zh'
    #     salt = random.randint(32768, 65536)
    #     sign = appid + q + str(salt) + secretKey
    #     m1 = hashlib.md5()
    #     m1.update(sign.encode())
    #     sign = m1.hexdigest()
    #     my_url = my_url + '?appid=' + appid + '&q=' + urllib.parse.quote(
    #         q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    #     try:
    #         r = requests.get(my_url)
    #         response = r.content
    #         json_data = json.loads(response)
    #         return json_data['trans_result'][0]['dst']
    #     except Exception as e:
    #         return str(e)

    def en2ch(self,q):
        # typ = sys.getfilesystemencoding()
        # C_agent = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.165063 Safari/537.36 AppEngine-Google."}
        # flag = 'class="t0">'
        # tarurl = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % ('zh', 'en', q.replace(" ", "+"))
        # request = urllib.request.Request(tarurl, headers=C_agent)
        # page = str(urllib.request.urlopen(request).read().decode('utf-8'))
        # target = page[page.find(flag) + len(flag):]
        # target = target.split("<")[0]
        # return target

        context = q
        url = 'http://fanyi.baidu.com/v2transapi/'
        data = {
            'from': 'en',
            'to': 'zh',
            'query': context,
            'transtype': 'translang',
            'simple_means_flag': '3',
        }
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'}

        flag = 1
        # 失败后最多重连20次
        while flag < 20:
            print('翻译>正在向网页发送第 ' + str(flag) + '次请求')
            try:
                response = requests.post(url, data, headers=headers)
                head = response.headers
                # print(head['Content-Type'])
                # print(response.json()['trans_result']['data'][0]['dst'])
                rst = response.json()['trans_result']['data'][0]['dst']
                flag = 200
            except:
                rst = ['翻译>翻译失败']
                flag = flag + 1




        return rst





