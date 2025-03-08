from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import New
from django.views.generic import ListView

# Простая вьюшка для отображения страницы

class NewsListView(ListView):
    model = New
    template_name = 'news/news.html'
    context_object_name = 'news'


