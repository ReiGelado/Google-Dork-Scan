import threading, urllib2
import Queue

urls_to_load = [
'http://stackoverflow.com/',
'http://slashdot.org/',
'http://www.archive.org/',
'http://www.yahoo.co.jp/',
]

def read_url(url, queue):
    data = urllib2.urlopen(url).read()
    print('Fetched %s from %s' % (len(data), url))
    queue.put(data)

def fetch_parallel():
    result = Queue.Queue()
    threads = [threading.Thread(target=read_url, args = (url,result)) for url in urls_to_load]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return result

def fetch_sequencial():
    result = Queue.Queue()
    for url in urls_to_load:
        read_url(url,result)
    return result
