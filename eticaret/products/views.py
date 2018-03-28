from django.shortcuts import render

# Create your views here.
from products.models import products


def index(request):
    product=products.objects.all()
    return  render (request,'index.html',locals())
