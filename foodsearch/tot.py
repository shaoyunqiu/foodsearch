import urllib2

response = urllib2.urlopen("https://en.wikipedia.org/wiki/List_of_salads")

html = response.read()
f = open("List_of_salads.html",'w')
f.write(html)
f.close()
print "saladtotal done"

response = urllib2.urlopen("https://en.wikipedia.org/wiki/List_of_cakes")

html = response.read()
f = open("List_of_cakes.html",'w')
f.write(html)
f.close()
print "cakestotal done"
