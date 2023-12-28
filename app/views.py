from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']

        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()

        QLTO=Topic.objects.all()
        d={'topics':QLTO}

        return render(request,'display_topic.html',d)
    return render(request,'insert_topic.html')

def insert_webpage(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}

    if request.method=='POST':
        tn=request.POST['tn']
        name=request.POST['n']
        url=request.POST['url']
        email=request.POST['em']

        TO=Topic.objects.get(topic_name=tn)

        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
        WO.save()

        QLWO=Webpage.objects.all()
        d1={'webpages':QLWO}
        return render(request,'display_webpage.html',d1)
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}

    if request.method=='POST':
        n=request.POST['n']
        au=request.POST['au']
        da=request.POST['da']

        WO=Webpage.objects.get(name=n)

        AO=AccessRecord.objects.get_or_create(name=WO,author=au,date=da)[0]
        AO.save()

        QLAO=AccessRecord.objects.all()
        d1={'access':QLAO}

        return render(request,'display_access.html',d1)
    return render(request,'insert_access.html',d)