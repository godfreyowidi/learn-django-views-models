from django.contrib import admin
from django.urls import path
from .views import home_view
from articles import views

urlpatterns = [
    path('', home_view),
    path('articles/<int:id>', views.articles_details_view),
    path('admin/', admin.site.urls),
]
