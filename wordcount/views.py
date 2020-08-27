from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request, 'home.html')

def count(request):
	fulltext = request.GET['fulltext']
	
	wordlist = fulltext.split()

	wordDictionary = {}

	for word in wordlist:
		if word in wordDictionary:
			wordDictionary[word] += 1
			#Increase
		else:
			#add to dictionary
			wordDictionary[word] = 1

	sortedWords = sorted(wordDictionary.items(), key = operator.itemgetter(1), reverse = True)

	return render(request, 'count.html', {'fulltext' : fulltext, 'count' : len(wordlist), 'sortedWords' : sortedWords})