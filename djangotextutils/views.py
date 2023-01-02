# i have created this file
from django.http import HttpResponse
from django.shortcuts import render

# Code for Laying the pipeline.
def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext =request.POST.get("text","default")

    #Check checkbox value
    removepunc =request.POST.get("removepunc","off")
    fullcaps =request.POST.get("fullcaps","off")
    newlineremover =request.POST.get("newlineremover","off")
    spaceremove =request.POST.get("spaceremove","off")


    if removepunc=="on":
        punctuations ='''!@#$%^&*()_-`~[]{}+=;:'",<>/\|'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params = {'purpose':'Remove Punctuation', 'analyzed_text':analyzed}
        djtext=analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        djtext=analyzed


    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'remove new line', 'analyzed_text': analyzed}
        djtext=analyzed


    if(spaceremove=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'space remove', 'analyzed_text': analyzed}

    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and spaceremove!="on"):
        return HttpResponse("<h1>Please select the operation</h1>")
    return render(request, 'analyze.html', params)
