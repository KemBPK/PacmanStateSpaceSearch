# from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from pacmanModule import pacman

def testpage(request):
    args = pacman.readCommand( [ '-l', 'mediumMaze', '-p', 'SearchAgent', '-a', 'fn=bestfs', '-t'] ) # Get game components based on input
    pacman.runGames( **args )
    return HttpResponse('test')

def landing(request):
    return render(request, 'webgraph/landing.html')