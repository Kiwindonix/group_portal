from django.shortcuts import render
from django.views.generic import ListView
from .models import MediaFile

class MediaListView(ListView):
    model = MediaFile
    template_name = "gallery/gallery.html" 
    context_object_name = "media_files"
    