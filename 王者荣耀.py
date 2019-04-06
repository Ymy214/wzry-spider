import requests
fo = open('./wzry-jpg/wzry-pf.txt', 'w')
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

path = './wzry-jpg/'
ls = []     
for i in range(105,200):
    url = "http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{0}/{0}-bigskin-1.jpg".format(i)
    status_code = requests.request('get', url).status_code
    if status_code != 200:
        continue
    for j in range(1, 9):
        imgurl = url[:-5] + '{}.jpg'.format(j)
        response = requests.request('get', imgurl)
        if response.status_code != 200:            
            continue
        ls.append(imgurl)
        ##下载
        print("开始下载第{}-{}个英雄皮肤图片>>>".format(i,j), end='')
        with open(path+str(i)+'-'+str(j)+'.png', 'wb') as f:
            f.write(response.content)
            print('======下载完成======')

    
for i in range(501,516):
    url = "http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{0}/{0}-bigskin-1.jpg".format(i)
    status_code = requests.request('get', url).status_code
    if status_code != 200:
        continue
    for j in range(1, 9):
        imgurl = url[:-5] + '{}.jpg'.format(j)
        response = requests.request('get', imgurl)
        if response.status_code != 200:            
            continue
        ls.append(imgurl)
        ##下载
        print("开始下载第{}-{}个英雄皮肤图片>>>".format(i,j), end='')
        with open(path+str(i)+'-'+str(j)+'.png', 'wb') as f:
            f.write(response.content)
            print('======下载完成======')
##print(ls)
        
##连接写入txt文件
for line in ls:
    fo.write(line+'\n')
fo.close()
