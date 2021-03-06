#!/usr/bin/python  
#coding=utf-8

'''自动爬取momentum每天的图片,并保存'''
  
import os  
import json  
import urllib2  
import urllib  
import time  
  
  
def auto_down(url, filename):  
    try:  
        urllib.urlretrieve(url, filename)  
    except urllib.ContentTooShortError:  
        print 'Network conditions is not good.\nReloading.'  
        auto_down(url, filename)  
  
  
directory = os.path.dirname(os.path.realpath(__file__)) + '/pictures/'  
print directory  
today = time.strftime("%Y-%m-%d")  
  
req = urllib2.Request('https://api.momentumdash.com/feed/bulk?syncTypes=backgrounds&localDate=' + today)  
req.add_header('Host', 'api.momentumdash.com')  
req.add_header('Accept', '*/*')  
req.add_header('X-Momentum-ClientId', '237eeecc-e1eb-490f-9a4c-94eafffeca1e')  
req.add_header('X-Momentum-Version', '0.91.1')  
req.add_header('Content-Type', 'application/json')  
  
response = urllib2.urlopen(req)  
  
data = json.loads(response.read())  
  
if not os.path.exists(directory):  
    os.makedirs(directory)  
  
for bg in data['backgrounds']:  
    # name = bg['filename'].rsplit('/', 1)[-1]  
    path = directory + today + ".png"  
    # print name  
    # no file type data, so assume .png  
    if not os.path.exists(path):  
        auto_down(bg['filename'], path)  
