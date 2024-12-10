from django.shortcuts import render
from . models import Articles
# Create your views here.
def index(req):
    data = Articles.objects.all()
    context = {
        'data':data
    }
    return render(req,'index.html',context)

def display(req,pk):
    data1 = Articles.objects.get(id = pk)
    context = {
        'data1' : data1
    }
    return render(req,'display.html',context)

def about(req):
    return render(req,'about.html')