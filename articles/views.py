from django.shortcuts import render

from .models import Articles


def article_search_view(request):
    # print(dir(request))
    # print(request.GET)
    query_dict = request.GET
    # query = query_dict.get('query')
    try:
        query = int(query_dict.get('query'))
    except:
        query = None

    article_obj = None
    if query is not None:
        article_obj = Articles.objects.get(id=query)
    context={
        "object": article_obj,
    }
    return render(request, "articles/search.html", context=context)

def article_create_view(request):
    # print(request.POST)
    context = {}
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        articles_obj = Articles.objects.create(title=title, content=content)
        print(title, content)
        context["object"] = articles_obj
        context["created"] = True
    return render(request, 'articles/create.html', context=context)

def articles_details_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Articles.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(request, 'articles/detail.html', context=context)