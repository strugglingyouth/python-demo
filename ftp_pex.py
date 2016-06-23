#！/usr/bin/python
#coding:utf-8
import pexpect
import sys

'''
    自动化ftp操作
'''

child = pexpect.spawnu('ftp 222.24.51.147')     #运行ftp，命令
child.expect('(?i)name .*:')                    #(?i)表示后面的字符串正则匹配忽略大小写
child.sendline('ftp')                   #输入ftp账号信息
child.expect('(?i)password')            #匹配提示符
child.sendline('ftp')                   #输入ftp密码 
child.expect('ftp> ')       
child.sendline('bin')                   #启用二进制模式
child.expect('ftp> ')
child.sendline('get vimrc')             #下载vimrc文件
child.expect('ftp> ')
sys.stdout.write(child.before)          #输出匹配'ftp>'之前的输入与输出
print("Escape character is '^]'.\n")
sys.stdout.write(child.after)
sys.stdout.flush()

child.interact()    #调用interact()让出控制权，用户可以继续当前的会话手工控制子程序
child.sendline('bye')
child.close()



