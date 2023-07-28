from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'name':'jamshed','age':3}
    return render(request,'data_render.html',context=d)

def conditions(request):
    d={'a':1000,'b':15000,'c':7000}
    return render(request,'conditions.html',context=d)
    