from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Articles
from .forms import ArticleForm


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


@login_required
def article_create_view(request):
    form = ArticleForm( request.POST or None )
    context = {
        "form": form,
    }
   
    if form.is_valid():
        articles_obj = form.save()
        context["form"] = ArticleForm()
        # title = form.cleaned_data.get("title")
        # content = form.cleaned_data.get("content")
        # articles_obj = Articles.objects.create(title=title, content=content)
        # context["object"] = articles_obj
        # context["created"] = True
    return render(request, 'articles/create.html', context=context)

def articles_details_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Articles.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(request, 'articles/detail.html', context=context)


# @login_required
# def article_create_view(request):
#     # print(request.POST)
#     form = ArticleForm()
#     context = {
#         "form": form,
#     }
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
#         context["form"] = form
#         if form.is_valid():
#             title = form.cleaned_data.get("title")
#             content = form.cleaned_data.get("content")
#             articles_obj = Articles.objects.create(title=title, content=content)
#             context["object"] = articles_obj
#             context["created"] = True
#     return render(request, 'articles/create.html', context=context)

# def articles_details_view(request, id=None):
#     article_obj = None
#     if id is not None:
#         article_obj = Articles.objects.get(id=id)
#     context = {
#         "object": article_obj,
#     }
#     return render(request, 'articles/detail.html', context=context)