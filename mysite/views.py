#i have created this website
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #return HttpResponse(''''<h1> suman </h1><a href= "https://brilliant.org/welcome/where-to-start/?tour=true#recommendations">
    #django book </a>''')
    params = {'name':'harry', 'place':'mars'}
    return render(request,'index2.html',params)


def about(request):
    return HttpResponse("about suman")

def removepunc(request):
    djtext = request.GET.get('text','default')
    return HttpResponse("removepunc")

def capitalizefirst(request):
    return HttpResponse("capitalize first")

def newlinerremover(request):
    return HttpResponse("new linner remover")

def spaceremover(request):
    return HttpResponse("space remover ,<a href='/capitalizefirst'>capitalize</a>")

def charcount(request):
    return HttpResponse("char count")

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlinerremover = request.GET.get('newlineremover', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')
    print(djtext)
    #analyzetext= djtext
    punc=";,./;'.;"
    analyzed=""
    for char in djtext:
        if char not in punc:
            analyzed = analyzed+ char
    params= {'purpose':'removepunc','analyzedtext':analyzed}
    if removepunc =="on":
      return render(request,'analyze.html',params)
    elif fullcaps== 'on':
        analyzed=""
        for char in djtext:
            analyzed= analyzed+char.upper()
        params= {'purpose':'Capitalize','analyzedtext':analyzed}
        return render(request, 'analyze.html', params)

    elif newlinerremover=='on':
        analyzed = ""
        for char in djtext:
            if char!='/n':
             analyzed = analyzed + char
        params = {'purpose': 'Remove new line', 'analyzedtext': analyzed}
        return render(request, 'analyze.html', params)
    elif spaceremover=='on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == ' ' and djtext[index+1]==' ':
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Remove new line', 'analyzedtext': analyzed}
        return render(request, 'analyze.html', params)
    elif charcount=='on':
        count=0
        for char in djtext:
            count= count+1
        params = {'purpose': 'character count', 'analyzedtext': count}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")