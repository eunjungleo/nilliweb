from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.db.models import Q


from collections import Counter

import os
import sys
import urllib.request

#display all items
class ContentsAll(ListView):
    model = Content
    template_name = "list.html"

# about team nilli
class AboutView(TemplateView):
    template_name = "about.html"

@csrf_exempt
# detailview
def detail_view(requests, pk):
    obj = get_object_or_404(Content, pk=pk)
    # get youtube id out of given url
    youtube_id = obj.youtube_url.split(".be/")[1]
    pl_url = 'https://www.youtube.com/embed/videoseries?list='+ obj.playlist_url.split("?list=")[1]

    #papago API
    if requests.method=='POST':
        userlang = requests.POST['lang']
        client_id = "ffa3jefjyn" 
        client_secret = "94AtTndnGXKtpckzXo05M8lARtZwuPvRDjKAutOz"
        encText = urllib.parse.quote(obj.korean)
        data = "source=ko&target="+ userlang + "&text=" + encText
        url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"
        request = urllib.request.Request(url)
        request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
        request.add_header("X-NCP-APIGW-API-KEY",client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()

        
        if(rescode==200):
            response_body = response.read()
            r = response_body.decode('utf-8')
            perf_r = r.split('"translatedText":')[1].split(',"engineType"')[0]
            
            return render(requests, "detail.html", {'youtube_id':youtube_id, 'pl_url':pl_url, 'obj':obj, 'perf_r':perf_r, 'userlang':userlang})

        else:
            err = print("Error Code:" + rescode)
            return render(requests, "detail.html", {'youtube_id':youtube_id, 'pl_url':pl_url, 'obj':obj, 'perf_r':perf_r, 'err':err, 'userlang':userlang})
        
    else:
        return render(requests, "detail.html", {'youtube_id':youtube_id, 'pl_url':pl_url, 'obj':obj, 'userlang':userlang})


#QUIZ
def quiz(requests):

    return render(requests, "quiz.html")

def match_vid(request):
    if request.method=='GET':
        q1_val = request.GET['q1'][0]
        q2_val = request.GET['q2'][0]
        q3_val = request.GET['q3'][0]
        q4_val = request.GET['q4'][0]
        q5_val = request.GET['q5'][0]

        sort1 = list(Content.objects.filter(q1=q1_val))
        sort2 = list(Content.objects.filter(q2=q2_val))
        sort3 = list(Content.objects.filter(q3=q3_val))
        sort4 = list(Content.objects.filter(q4=q4_val))
        sort5 = list(Content.objects.filter(q5=q5_val))

        # concat results
        sorts = sort1 + sort2 + sort3 + sort4 + sort5

        # order items by frequency
        result_raw = [item for items, i in Counter(sorts).most_common() for item in [items] * i] 

        # de-duplicate
        result = []
        for elem in result_raw:
            if elem not in result:
                result.append(elem)
        
        result = result[:4]


    return render(request, "list.html", { 'result':result})

# map
def mapview(requests):
    return render(requests, 'map.html')

# map list
def country_view(requests, option):
    content = None

    if option=='tm':
        content = Content.objects.filter(id__range=(1,3))
    elif option=='cn':
        content = Content.objects.filter(id__range=(4,6))
    elif option=='kr':
        content = Content.objects.filter(id__range=(7,8))
    elif option=='at':
        content = Content.objects.filter(id=9)

    return render(requests, "list.html", {'content':content})
