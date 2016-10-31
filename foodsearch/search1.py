from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader,Context
from django.shortcuts import render
from keywords import searchdic, filedic, namedic, contdic
import re

key = ""
searchlist = []
pagelist = []

@csrf_exempt

def index(request): 
	#global key
    if request.method == "POST":
        Search(request, 1, request.POST['key'])
        response = HttpResponse(content_type='text/html')
        t = loader.get_template('saladlist.html')
        c = Context({"key":key, "searchlist":searchlist, "pagelist":pagelist})
        response.write(t.render(c))
        return response
    else:
    	if not request.GET.has_key('p'):
    		#return HttpResponse(text)
    		return render(request, "saladindex.html")
    	else:
    		Search(request, int(request.GET['p'].strip()), key)
    		response = HttpResponse(content_type='text/html')
        	t = loader.get_template('saladlist.html')
        	c = Context({"key":key, "searchlist":searchlist, "pagelist":pagelist})
        	response.write(t.render(c))
        	return response


@csrf_exempt
def Search(request, page, k):
	global key
	global searchlist
	global pagelist
	key = k
	tmp = key
	searchlist = []
	pagelist = []
	tmp = tmp.lower()
	p = re.compile('[a-z]+')
	l = p.findall(tmp)
	if len(l) == 0:
		return
	allidset = set()
	for word in l:
		if  searchdic.has_key(word):
			idlist = searchdic[word]
			allidset.update(idlist)
	tmpidlist = list(allidset)
	allidlist = []
	for number in tmpidlist:
		if number <= 52:
			allidlist.extend([number])
	tol_page = len(allidlist)  / 10 + 1
	for i in range(1, tol_page+1):
		pagedic = {}
		pagedic['url'] = "http://127.0.0.1:8000/salad/?p=%d" % i
		pagedic['num'] = i 
		pagelist.append(pagedic)
	if tol_page < page:
		return 
	cnt = 0
	for id in allidlist:
		cnt += 1
		if cnt < (page-1)*10+1 or cnt > page*10 :
			continue
		else:
			dic = {}
			dic['url'] = filedic[id]
			dic['content'] = contdic[id]
			dic['name'] = namedic[id][:-7]
			searchlist.append(dic)

