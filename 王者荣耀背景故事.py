#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
fo = open('R:/python123全国等考/wzry-jpg/pop-bd.txt', 'w')
##fi = open("bilibili.txt", "r")
##path = './bilibili-png/'
##
##txt = fi.read()
##txt = txt.split('background-image')
##ls = []
##for l in txt:
##    if '.png' in l:
##        l = l.split('url')[1].split('"')[1]
##        ls.append(l)
#### 图片url放入list列表


ls = []     
for i in range(105,200):
    url = "https://pvp.qq.com/web201605/herodetail/{}.shtml".format(i)
    r = requests.request('get', url)
    if r.status_code != 200:
        continue
    r.encoding = 'gbk'
    name = r.text.split('cname')[1].split(',')[0].split("'")[1]
    text = r.text.split('pop-bd')[1].split('p>')[1][:-2]
    print("开始保存第{}个英雄背景故事>>>".format(i))
    fo.write('【'+name+'】'+'\n'+text+'\n'+'-'*30)

for i in range(501,516):
    url = "https://pvp.qq.com/web201605/herodetail/{}.shtml".format(i)
    r = requests.request('get', url)
    if r.status_code != 200:
        continue
    r.encoding = 'gbk'
    name = r.text.split('cname')[1].split(',')[0].split("'")[1]
    text = r.text.split('pop-bd')[1].split('p>')[1][:-2]
    print("开始保存第{}个英雄背景故事>>>".format(i))
    fo.write('【'+name+'】'+'\n'+text+'\n'+'-'*30)

##连接写入txt文件

fo.close()

        



