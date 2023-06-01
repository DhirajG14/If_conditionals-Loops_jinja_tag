from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':10,'b':20,'c':40}
    return render(request,'conditions.html',context=d)

def loops(request):
    dict={'name1':'Kushal','name2':''}
    return render(request,'loops.html',dict)