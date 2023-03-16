from django.shortcuts import render

# Create your views here.

def dhoni(request):
    return render(request,'dhoni.html')


def devilers(request):
    return render(request,'devilers.html')