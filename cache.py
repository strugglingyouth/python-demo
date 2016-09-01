#!/usr/bin/env python
# coding:utf-8



def func_cache(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print 'wrapper:',args
            print 'in cache'
            return cache[args]
        else:
            res = func(*args)
            cache[args] = res
            return res
    print cache
    return wrapper


@func_cache
def add(a,b):
    return a + b

if __name__ == '__main__':
    print add(1,2)
    print add(1,2)
    print add(3,4)








