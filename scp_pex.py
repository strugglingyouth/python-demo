#!/usr/bin/python
#coding:utf-8
import pexpect
import sys

'''
    远程文件自动打包并下载
'''

ip = '222.24.51.147'
user = 'root'
passwd = 'xxxxxx'
target_file = '/var/log/boot.log'   #目标主机文件
    
child = pexpect.spawn('/usr/bin/ssh',[user+'@'+ip]) #运行ssh命令
fout = open('mylog','wb')
child.logfile = fout

try:
    child.expect('(?i)password')    #匹配password
    child.sendline(passwd)
    child.expect('#')
    child.sendline('tar cf /var/log/feiyu.tar.gz '+target_file)     #打包目标文件
    child.expect('#')
    print(child.before)
    child.sendline('exit')
    fout.close()
except EOF:                 #定义EOF异常处理
    print('except EOF!')
except TIMEOUT:             #定义TIMEOUT异常处理
    print('except TIMEOUT!') 
child = pexpect.spawn('/usr/bin/scp root@222.24.51.147:/var/log/feiyu.tar.gz .')
fout = open('scplog','ab')
child.logfile = fout
try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect(pexpect.EOF)
except EOF:
    print('expect EOF!')
except TIMEOUT:
    print('expect TIMEOUT!')    
    



    
    

    
    
    
    
    
    
    


