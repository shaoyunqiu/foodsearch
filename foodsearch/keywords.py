#encoding=utf-8
from bs4 import BeautifulSoup
import re
import copy
import sys
from htmlentitydefs import name2codepoint
reload(sys)
sys.setdefaultencoding('utf-8')

filedic = {}#id, url dictionary
namedic = {}#id , filename dictionary
f = open("D:\\python\\foodsearch\\foodsearch\\saladId.txt",'r')
filelist = f.readlines()
for line in filelist:
	line = line.split("@@")
	url = line[0]
	id = int(line[1].strip())
	filedic[id] = url
	name = url.split('/')[-1] + '_' + str(id) + '.html'
	namedic[id] = name
	saladend = id
f.close()
#print filedic
print "salad dict finished" 

f = open("D:\\python\\foodsearch\\foodsearch\\cakeId.txt", 'r')
filelist = f.readlines()
for line in filelist:
	line = line.split("@@")
	url = line[0]
	id = int(line[1].strip())
	name = url.split('/')[-1] + '_' + str(id) + '.html'
	filedic[id] = url
	namedic[id] = name
	cakeend = id

f.close()
#print filedic
#print saladend, cakeend
#print namedic
print "cake dict finished"

keyset = set() #all the keywords , type set
setdic = {} # each id a keyword
contdic = {} # each id a content
p = re.compile('[a-z]+', re.I)
#c = 0
for i in range(1, saladend+1):
	html = open("D:\\python\\foodsearch\\foodsearch\\salad\\" + namedic[i]).read()
	#c += 1
	soup = BeautifulSoup(html,'html.parser')
	text = ""
	first = soup.find('p').get_text()
	#fp = re.compile('([^\w*]|\d*)')
	fp = re.compile(r'\[\d*\]')
	contdic[i] = fp.sub(" ", first)
	for item in soup.find_all('p'):
		text += item.get_text() + " "
	#tmp = text[500:1000]
	text = text.lower()
	wordlist = p.findall(text)
	keyset.update(wordlist)
	setdic[i] = set(wordlist[:])
	#contdic[i] = tmp
	#print "set a salad file" , c
print "salad keyset and setdic and contdic finished"
#print keyset
#c = 0
for i in range(101, cakeend+1):
	html = open("D:\\python\\foodsearch\\foodsearch\\cake\\"+ namedic[i]).read()
	#c += 1
	soup = BeautifulSoup(html,'html.parser')
	text = ""
	first = soup.find('p').get_text()
	fp = re.compile(r'\[\d*\]')
	#fp = re.compile('([^\w*]|\d*)')
	contdic[i] = fp.sub(" ", first)
	for item in soup.find_all('p'):
		text += item.get_text()+ " "
	#tmp = text[500:1000]
	text = text.lower()
	wordlist = p.findall(text)
	keyset.update(wordlist)
	setdic[i] = set(wordlist[:])
	#contdic[i] = tmp
	#print "set a cake file" , c
print "cake keyset and setdic contdic finished"
print len(keyset)

keylist = list(keyset)
searchdic = {} #{key, idlist[]}
#c = 0
for i in range(0, len(keyset)):
	#c += 1
	word = keylist[i] #read through each word in the keyset
	wordpagelist = []
	for j in range(1, saladend+1):
		#idset = setdic[j]
		if word in setdic[j]:
			wordpagelist.extend([j])
		else:
			pass
	for j in range(101, cakeend+1):
		#idset = setdic[j]
		if word in setdic[j]:
			wordpagelist.extend([j])
		else:
			pass
	searchdic[word] = wordpagelist[:]
	#print "a word list" , c

print "searchdic finished"

'''class Info:
	def __init__(self):
		self.filedic = copy.deepcopy(filedic)
		self.namedic = copy.deepcopy(namedic)
		self.searchdic = copy.deepcopy(searchdic)
		self.contdic = copy.deepcopy(contdic)'''

#i = Info()
#print "Info.searchdic", i.searchdic['cake']

