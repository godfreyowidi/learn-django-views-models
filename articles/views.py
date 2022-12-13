from django.shortcuts import render

from .models import Articles

def articles_details_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Articles.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(request, 'articles/detail.html', context=context)