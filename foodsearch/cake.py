#!/usr/bin/env python 
#coding=utf-8 
import urllib2
from HTMLParser import HTMLParser
res = "List_of_cakes.html"

class myParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.head = "https://en.wikipedia.org"
        self.cnt = 100
    def handle_starttag(self, tag, attrs):
        #print "snach the salad page"
        if tag == 'a':
            if len(attrs) == 0:
                return 
            else:
                for(key, value) in attrs:
                    if key == "href":
                        if type(value) == type(None):
                            return
                        urltail = value
                        if urltail.find('cake') == -1:
                            #pass
                            #print "no cake ,pass"
                            return 
                        if urltail[:6] != "/wiki/":
                            return
                        if urltail[-4:] == '.jpg':
                            return
                        else:
                            #print "snach the page"
                            self.cnt += 1
                            url = self.head + urltail
                            response = urllib2.urlopen(url)
                            page = response.read()
                            filename = 'cake//'+urltail.split('/')[-1] + '_'+ str(self.cnt)+'.html'
                            f = open(filename,'w')
                            f.write(page)
                            f.close()
                            f = open("cakeId.txt",'a')
                            info = url + "@@" + str(self.cnt) + '\n'
                            f.write(info)
                            f.close()
                            print "snach the page" , self.cnt
                            #if(self.cnt >= 110):
                                #print "stop"
                                #return
                            #print snatch a page

hp = myParser()
hp.feed(open(res).read())
hp.close()
print 'done'
