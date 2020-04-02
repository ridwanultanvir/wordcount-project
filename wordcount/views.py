from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')


def aboutfunc(request):
    return render(request, 'about.html')


def mark(request):
    return HttpResponse('<h1> Your mark is 0 </h1>')


"""
[02/Apr/2020 12:52:41] "GET / HTTP/1.1" 200 219
TIP TOP
TIK TOK
WE ARE IN 1111111111111111111111111111111111111111111

in command line printed

"""
def countfunc(request):
    fulltext = request.GET['textarea_name']
    print(fulltext)
    wordlist = fulltext.split()


    worddictionary= {}


    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedlist = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'mycount.html', {'reftext':fulltext, 'lenwordlist':len(wordlist),'refsortedlist': sortedlist})
