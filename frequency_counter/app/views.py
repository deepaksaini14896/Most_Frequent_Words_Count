from django.shortcuts import render
from .models import encountered_url
import html2text
import urllib.request


# Create your views here.

def frequency(request):
	return render(request,'form.html')

def result(request):
	if request.method == 'POST':
		words_object=encountered_url.objects.filter(url=request.POST['url_request'])
		
		if words_object.exists():
			return render(request,'result.html',{'dicts':words_object, 'data':'Data is coming from the database.'})
	
		url=urllib.request.urlopen(request.POST['url_request'])
		common_words=urllib.request.urlopen("https://raw.githubusercontent.com/deepaksaini14896/100_common_words/main/100_common_words.txt")
		syntax_and_numbers=urllib.request.urlopen("https://raw.githubusercontent.com/deepaksaini14896/syntax_and_numbers/main/syntax%26numbers.txt")
		page=""
		words=[]
		syntax_numbers=[]
		
		for i in url.readlines():
			page+=i.decode('utf-8')

		for i in common_words.readlines():
			words.append(i.decode('utf-8').rstrip())

		for i in syntax_and_numbers.readlines():
			syntax_numbers.append(i.decode('utf-8').rstrip())

		text_maker = html2text.HTML2Text()
		text_maker.ignore_links = True
		text_maker.ignore_images = True
		text = text_maker.handle(page)
		dic={}
		temp=""

		for i in text:
			i=i.rstrip()

			if i not in syntax_numbers:
				temp+=i

			else:

				if temp!='':

					if temp in words:
						temp=""

					else:
						if temp in dic.keys():
							dic.update({temp:dic[temp]+1})

						else:
							dic[temp.lower()]=0
							temp=""

		sorted_keys=sorted(dic,key=dic.get)
		count=0

		for i in sorted_keys[::-1]:
			
			if count==10:
				break
			
			count+=1
			q=encountered_url(url=request.POST['url_request'],word=i,count=dic[i])
			q.save()

		words_object=encountered_url.objects.filter(url=request.POST['url_request'])
		return render(request,'result.html',{'dicts':words_object, 'data':'Data is freshly processed.'})

	else:
		return 	render(request,'form.html')
