from django.shortcuts import render

# Create your views here.
def wish(request,name):
    params={
        'n':name
    }
    return render(request,'wish.html',params)
