from django.http import HttpResponse
from django.shortcuts import render
import operator

def homePage(request):
    return render(request,'home.html')
def count(request):
    fulltext=request.GET["fulltext"]
    wordlist=fulltext.split()
    length=len(wordlist)
    #word analysis
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #increament
            worddictionary[word] += 1
        else:
            #add to worddictionary
            worddictionary[word] = 1
        sortedWords = sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'length':length,'sortedWords':sortedWords})
def about(request):
    return render(request,'about.html')
