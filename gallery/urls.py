from django.urls import path
from .views import MediaListView

urlpatterns = [
    path('gallery/', MediaListView.as_view(), name='gallery'),
]