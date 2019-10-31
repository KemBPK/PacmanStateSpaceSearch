# from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .pacmanModule import pacman

def testpage(request):
    return HttpResponse('test')