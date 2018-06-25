# -*- coding: utf-8 -*-
# @Time             :  2018/2/18 14:10
# @Author           :  lenovo;
# @project_name     :  Music
# @File             :  lyric.py
# @Software         :  PyCharm
# @belong to file   :  
 
import requests
import execjs
import json

header={
    'Cookie':'_ntes_nuid=16a42b02260b7b091899fdfe44ee36d5; __f_=1517818018835; vjuids=-384d52583.16168b64799.0.90747366b31e8; vjlast=1517880232.1517880232.30; _ntes_nnid=16a42b02260b7b091899fdfe44ee36d5,1517880231840; vinfo_n_f_l_n3=d71018b33b6778e8.1.0.1517880231854.0.1517880258969; JSESSIONID-WYYY=uOVEcIJi3PyQpmZq4tYHNt8NfH9FOj4cCUson4NE4%2F%2FiqMJxNlclpuPNceaFBRU%2F5%2FmM4JriGz3l9Cg1BEwxsrENOZjQKFAVHh%2BwxEK%2FC2uJ782JKeI9EFCG8xEbp3Y4Rf3J4DwJEQMHiN5nKAjxKQeo1TihQxXcJH3dUQyx%5CG8AGa6i%3A1518769837399; _iuqxldmzr_=32; __utma=94650624.744896615.1518768038.1518768038.1518768038.1; __utmb=94650624.4.10.1518768038; __utmc=94650624; __utmz=94650624.1518768038.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    'Origin':'http://music.163.com',
    'Referer':'http://music.163.com/search/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4785.400 QQBrowser/9.7.12991.400',

}

url='http://music.163.com/weapi/song/lyric?csrf_token='



with open('core1.js','r') as f:
    js_code=f.read()

song_id='479408220'

p2='010001'
p3='00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
p4='0CoJUm6Qyw8W8jud'


# {"id":"483671599","lv":-1,"tv":-1,"csrf_token":""}
p=execjs.compile(js_code).call('d', '{"id":"'+song_id+'","lv":-1,"tv":-1,"csrf_token":""}',p2,p3,p4)

print(p['encText'])
p1=p['encText']
print(p['encSecKey'])


data={
    'params':p['encText'],
    'encSecKey':p['encSecKey'],
}


response=requests.post(url,data=data,headers=header)

# 打印获取到数据
content = response.text
print(content)

content=json.loads(content)
content=content['lrc']['lyric']

# 歌词
print(content)

