from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext=request.GET['fulltext']

    word_list = fulltext.split()
    words=[]
    for word in word_list:
        if word in words:
            continue
        else:
            words.append(word)
    count=[]

    for word in words:
        i=0
        if word in word_list:
            for j in range(len(word_list)):
                if word_list[j]==word:
                    i+=1
            count.append(i)

    return render(request, 'count.html',{'fulltext': fulltext, 'count': len(word_list),'words': words,'word_count':count,'terms':len(count)})

def about(request):
    return render(request,'about.html')
