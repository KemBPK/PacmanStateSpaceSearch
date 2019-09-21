# from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

def testpage(request):
    return HttpResponse('test')