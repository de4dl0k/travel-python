from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import place1


# Create your views here.


def sample(request):
    obj = place.objects.all()
    obj1 = place1.objects.all()
    # name = 'sarang'
    return render(request, "index.html", {'result': obj, 'result1': obj1})


# def addition(request):
#
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res = x+y
#     return render(request, 'result.html', {'result': res})
