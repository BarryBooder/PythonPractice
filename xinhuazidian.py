#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
from urllib import urlencode


# ----------------------------------
# 新华字典调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/156
# ----------------------------------

def main():
    # 配置您申请的APPKey
    appkey = ""

    # 1.根据汉字查询字典
    request1(appkey, "GET")

    # 2.汉字部首列表
    request2(appkey, "GET")

    # 3.汉字拼音列表
    request3(appkey, "GET")

    # 4.根据部首查询汉字
    request4(appkey, "GET")

    # 5.根据拼音查询汉字
    request5(appkey, "GET")

    # 6.根据id查询汉字完整信息
    request6(appkey, "GET")


# 根据汉字查询字典
def request1(appkey, m="GET"):
    url = "http://v.juhe.cn/xhzd/query"
    params = {
        "word": "",  # 填写需要查询的汉字，UTF8 urlencode编码
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print
            res["result"]
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"


# 汉字部首列表
def request2(appkey, m="GET"):
    url = "http://v.juhe.cn/xhzd/bushou"
    params = {
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print
            res["result"]
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"


# 汉字拼音列表
def request3(appkey, m="GET"):
    url = "http://v.juhe.cn/xhzd/pinyin"
    params = {
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print
            res["result"]
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"


# 根据部首查询汉字
def request4(appkey, m="GET"):
    url = "http://v.juhe.cn/xhzd/querybs"
    params = {
        "word": "",  # 填写需要查询的汉字部首，UTF8 urlencode编码
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json
        "page": "",  # 页数，默认1
        "pageszie": "",  # 每页返回条数，默认10 最大50
        "isjijie": "",  # 是否显示简解，1显示 0不显示 默认1
        "isxiangjie": "",  # 是否显示详解，1显示 0不显示 默认1

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print
            res["result"]
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"


# 根据拼音查询汉字
def request5(appkey, m="GET"):
    url = "http://v.juhe.cn/xhzd/querypy"
    params = {
        "word": "",  # 填写需要查询的拼音
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json
        "page": "",  # 页数，默认1
        "pageszie": "",  # 每页返回条数，默认10 最大50
        "isjijie": "",  # 是否显示简解，1显示 0不显示 默认1
        "isxiangjie": "",  # 是否显示详解，1显示 0不显示 默认1

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print
            res["result"]
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"


# 根据id查询汉字完整信息
def request6(appkey, m="GET"):
    url = "http://v.juhe.cn/xhzd/queryid"
    params = {
        "word": "",  # 填写需要查询的汉字id
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print
            res["result"]
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"


if __name__ == '__main__':
    main()