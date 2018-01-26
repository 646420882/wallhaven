# coding:utf-8
import requests
import re
import sys
keyword = "girl"
class Wallhaven:
    def __init__(self):
        self.index_url = 'https://alpha.wallhaven.cc/search?q='+keyword+'&search_image='
        #self.start_url = 'https://alpha.wallhaven.cc/search?q='+keyword+'&search_image=&page='+str(page)
    def get_html(self,url):
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return r.text
            print(r.status_code)
        except:
            print('获取%s失败' % self.start_url)
            sys.exit()
    def get_pages(self):
        html = self.get_html(self.index_url)
        pattern1 = re.compile('class="fa fa-search search"></i>(.*?) Wallpapers found', re.S)
        pic_num =  re.findall(pattern1,html)
        if pic_num == 0:
            print('未找到相关图片')
            sys.exit()
        elif pic_num <= 24:
            pages = [1, 1]
        else:
            pattern = re.compile('class="thumb-listing-page-num">(\d+)</span> / (\d+)</h2>', re.S)
            pages = re.findall(pattern, html)[0]
        print('当前第%s页，共%s页,共%s张图片'%(pages[0],pages[1],pic_num))
    def main(self):
        self.get_pages()

app = Wallhaven()
app.main()