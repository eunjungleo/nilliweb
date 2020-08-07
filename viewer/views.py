from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404


class ContentsAll(ListView):
    model = Content
    template_name = "list.html"


class AboutView(TemplateView):
    template_name = "about.html"

# detailview
def detail_view(requests, pk):
    obj = get_object_or_404(Content, pk=pk)
    youtube_id = obj.url.split("/", 3)[3]
    return render(requests, "detail.html", {'youtube_id':youtube_id, 'obj':obj})