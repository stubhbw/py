# encoding:utf-8
# 网页爬虫

import re
import urllib


def getHtml(url):
    return urllib.urlopen(url).read()


def getImg(html):
    # src="//www.baidu.com/img/bd_logo1.png"
    # r1 = r'src="(.*?\.png)"'
    r1 = r'src="//(.*?\.png)"'
    imgRe = re.compile(r1)

    print(imgRe.findall(html))

    x = 0
    for i in imgRe.findall(html):
        fileName = "图片%s.png" % x
        print(fileName)
        urllib.urlretrieve('http://' + i, fileName)
        x += 1
    print "Download Pictures!!!"


html = getHtml("https://www.baidu.com/")
# html = getHtml("https://daohang.qq.com/?fr=hmpage")
getImg(html)
