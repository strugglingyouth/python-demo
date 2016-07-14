#!/usr/bin/env python
# coding=utf-8

import hashlib
import itertools

passwd = 'e10adc3949ba59abbe56e057f20f883e'  #'123456' 的加密结果

seed_dict = range(10)

for i in itertools.product(seed_dict,repeat=6):  # 对 0-9 进行排列组合，取6位
    result = ''.join(map(str,i))  # 转化为字符串
    value = hashlib.new("md5",result).hexdigest()  # 加密
    if result == '123456':
        print result
    #if hashlib.new("md5",result).hexdigest() == passwd:
    #    print '==',passwd
    if value == passwd:
        print '==',passwd
        print 'value:',value









