from django.shortcuts import render
from project import model

# Create your views here.

def index(request):
    return render(request, 'index.html')

def check(request):
    if request.method=="POST":
        data = request.POST['msg']
        result = None
        if data:
            result = model.main(data)
    return render(request, 'result.html', {"category": result,})
        
