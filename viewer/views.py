from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, TemplateView


class ContentsAll(ListView):
    model = Content
    template_name = "list.html"


class ContentDetail(DetailView):
    model = Content
    template_name = "detail.html"

class AboutView(TemplateView):
    template_name = "about.html"

