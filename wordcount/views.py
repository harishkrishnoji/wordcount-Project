from django.http import HttpResponse
from django.shortcuts import render
import operator

#def home(request):
#	return HttpResponse('Hello')

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def eggs(request):
	return HttpResponse('Harish love Eggs')

def count(request):
	fulltext = request.GET['fulltext']
	wordcount = fulltext.split()

	worddictionay = {}

	for word in wordcount:
		if word in worddictionay:
			worddictionay[word] += 1
		else:
			worddictionay[word] = 1

	sortedwords = sorted(worddictionay.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html', {'fulltext':fulltext, 'wordcount':len(wordcount), 'worddictionay':sortedwords })