#conding:utf8


from urllib.request import urlopen
from urllib.request import Request



class Write_to_file(object):
    def __init__(self):
        self.ok = 'ok'

    def write_to_txt(self, filename,count,title_en,abstract_en,title_cn,abstract_cn,new_url):
        # 将列表写入txt文件
        file_txt = open(filename, 'a', encoding='utf8')
        file_txt.write('【' + str(count) + '】:  '
                       'title: '+ title_en + '\n'
                        '题目: ' + title_cn + '\n'
                       'abstract: ' + abstract_en + '\n'
                       '摘要: '+ abstract_cn + '\n'
                       '链接:' + new_url + '\n\n')

    def download_pdf(self,url_pdf,name_pdf):
        req = Request(url_pdf)
        req.add_header("Host", "www.sciencedirect.com")
        req.add_header("User-Agent",
                       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")

        flag = 1
        while flag < 20:
            try:
                print('下载pdf>正在向网页发送请求')
                resp = urlopen(req, timeout=100)
                flag = 200
                f  = open(name_pdf, 'wb')
                f.write(resp.read())
                f.close()

            except:
                print('下载pdf>网络出了问题，第 %s 次重连' % str(flag))
                flag = flag + 1
                new_urls = []
                if flag > 20:
                    print('检索页>放弃爬取')