from django.shortcuts import render

# Create your views here.
def HomeWork(request):
    return render(request, "HW/ind.html")