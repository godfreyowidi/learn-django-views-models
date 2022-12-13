from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Articles
import random

def home_view(request, *args, **kwargs):

    name = "Godfrey"
    number = random.randint(1, 4)
    article_obj = Articles.objects.get(id=number)
    article_queryset = Articles.objects.all()
    context = {
        "object_list": article_queryset,
        "article_obj": article_obj,
        "title": article_obj.title,
        "content": article_obj.content,
        "id": article_obj.id,
    }
    HTML_STRING = render_to_string("home-view.html", context=context, )
    # HTML_STRING = """
    #     <h4>{title} - {id}</h4>
    #     <p>{content}</p>
    # """.format(**context)
    return HttpResponse(HTML_STRING)