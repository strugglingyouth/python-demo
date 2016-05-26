#!/usr/bin/env python2.7
# coding=utf-8

import requests
from Queue import Queue
import time 
import threading

from pyquery import PyQuery as pq

link_q = Queue()
dom_q = Queue()
links = set()

#base_domain = 'http://m.sohu.com'
base_domain = 'https://blog.linuxeye.com/'

def store(title,link):
    with open('./links.txt','ab') as f:
        f.write('%s  %s\n' %(title,link.encode('utf-8')))


def parse_links(dom):
    pq_dom = pq(dom)
    for link in pq_dom("a"):
        #import pdb;pdb.set_trace()
        pq_ele = pq(link)
        store(pq_ele.attr['href'],pq_ele.text())
        #store(link.values()[0],link.text_content())

class ProducerThread(threading.Thread):
    def run(self):
        while True:
            try:
                dom = dom_q.get(timeout=60)
            except Exception as e:
                print e
                break

            pq_dom = pq(dom)
            print '[produce]consume dom'
            for link in pq_dom("a"):
                pq_ele = pq(link)

                href = pq_ele.attr['href']
                if not href:
                    continue
                if not href.startswith('http'):
                    href = base_domain + href 
                
                store(href, pq_ele.text())

                print '[producer]produce', href 
                if href not in links: 
                    link_q.put(href)
                    links.add(href)

class ConsumerThread(threading.Thread):
    def run(self):
        while True:
            try:
                link = link_q.get(timeout=60)
            except Exception as e:
                print e
                break
            res = requests.get(link)
            print '[consumer]consume', link
            print '[consumer]produce dom'
            dom_q.put(res.content)
        
def main():
    # TODO:movie to 
    url = 'https://blog.linuxeye.com/'
    link_q.put(url)

    consumer = ConsumerThread()  #消费者生产dom
    consumer.setDaemon(1)
    consumer.start()

    producer = ProducerThread()  #生产者拿dom生产url
    producer.setDaemon(1)
    producer.start()

    while True:
        time.sleep(1)


if __name__ == '__main__' :
    print 'start-->'
    main()
