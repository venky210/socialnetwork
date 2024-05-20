from django.shortcuts import render,redirect

# Create your views here.

def slack(request):
    return render(request,'slack.html')




def addpeople(request):
    return render(request,'addpeople.html')