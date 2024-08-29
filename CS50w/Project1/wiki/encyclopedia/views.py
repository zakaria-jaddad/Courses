from django.shortcuts import render

from django.forms import forms

from django.utils.safestring import mark_safe

import markdown2

import random

from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse

from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def page(request, page):
    # converting to markdown2
    entry = util.get_entry(page)
    if entry:
        entry = markdown2.markdown(entry)
    entry = mark_safe(entry)
    return render(request, "encyclopedia/page.html", {
        "page": page, 
        "content": util.get_entry(page), 
        "text": entry
    })

    # ? Take the input from the html page 
    # ? Procces it and store it in a variable 
    # ? check if the page exist 
    # ? return a redirect to the page 

def search(request):
    if request.method == 'POST':
        form = request.POST.get('q')
        # if form not in util.list_entries():
        #     return 
        if util.get_entry(form):
            return HttpResponseRedirect(form)
        else:
            entries = []
            for content in util.list_entries():
                if form.upper() in content.upper():
                    entries.append(content)
            return render(request, "encyclopedia/index.html", {
                "entries": entries
            })
        
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        # checking 
        if not title or not content:
            return render(request, "encyclopedia/apology.html", {
                "error": "Provide title Or content"
            })
        # if the page already exist 
        if title.upper() in (X.upper() for X in util.list_entries()):
            return render(request, "encyclopedia/apology.html", {
                "error": "This Page is already exist"
            })
        
        # if it is new
        util.save_entry(title, content)
        return HttpResponseRedirect(title)
        
    else:
        return render(request, "encyclopedia/create.html")
    

def edit(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        # ! chainging the content of the page using the save_entry function
        util.save_entry(title, request.POST.get('content'))
        return HttpResponseRedirect(title)
    else:
        return render(request, "encyclopedia/edit.html", {
            "title": request.GET.get('title'),
            "content": request.GET.get('content')
        })
    

def random_entrie(request):
    entries = util.list_entries()
    # ! len entries is -1 indexet
    random_page = random.randint(0, len(entries) - 1)
    return HttpResponseRedirect(entries[random_page])