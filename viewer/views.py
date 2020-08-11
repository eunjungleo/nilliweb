from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404
from django.db.models import Q


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

#QUIZ
def quiz(requests):

    """
    # Q1. filter: eros vs. non eros

    filter1 = Content.objects.filter(eros)



    # Q2. filter: happy vs. not happy


    # redirect to detail page
    """
    return render(requests, "quiz.html")

def match_vid(request):
    if request.method=='GET':
        q1_val = request.GET['q1'][0]
        q2_val = request.GET['q2'][0]
        q3_val = request.GET['q3'][0]
        q4_val = request.GET['q4'][0]
        q5_val = request.GET['q5'][0]

        sort = Content.objects.filter(Q(q1=q1_val)|Q(q2=q2_val)|Q(q3=q3_val)|Q(q4=q4_val)|Q(q5=q5_val))
        sort = set(sort)
        items = list(sort)
        
        obj=None
        for obj in items:
            title = obj.title

        # order
        counts = [q1_val, q2_val, q3_val, q4_val, q5_val]
        counts = [ int(i) for i in counts ] 
        scores = sum(counts)

    
    return render(request, "list.html", {'items':items, 'obj':obj})