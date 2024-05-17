from django.shortcuts import render,redirect

# Create your views here.

def slack(request):
    return render(request,'slack.html')


def editchannel(request):
    if request.method=='POST':
        return redirect('slack')
    return render(request,'editchannel.html')


def addpeople(request):
    return render(request,'addpeople.html')