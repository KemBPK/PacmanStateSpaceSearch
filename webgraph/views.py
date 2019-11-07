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
    args = pacman.readCommand( [ '-l', 'mediumMaze', '-p', 'SearchAgent', '-a', 'fn=bestfs', '-t'] ) # Get game components based on input
    game = pacman.runGames( **args )
    # print pacman navigating through the maze 
    # for x in game[0]:
    #     print(x)
    # print('Average Score:', sum(game[1]) / float(len(game[1])))
    # print('Scores:       ', ', '.join([str(game[1]) for score in game[1]]))
    # print('Win Rate:      %d/%d (%.2f)' % (game[2].count(True), len(game[2]), game[3]))
    # print('Record:       ', ', '.join([ ['Loss', 'Win'][int(w)] for w in game[2]]))
    return render(request, 'webgraph/landing.html')