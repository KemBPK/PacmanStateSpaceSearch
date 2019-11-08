# from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from pacmanModule import pacman
import json
from cgi import parse_header
from pacmanModule.maze import Maze
from pacmanModule.layout import change_char

def testpage(request):
    args = pacman.readCommand( [ '-l', 'mediumMaze', '-p', 'SearchAgent', '-a', 'fn=bestfs', '-t'] ) # Get game components based on input
    pacman.runGames( **args )
    return HttpResponse('test')

def landing(request):
    # maze = Maze.generate(30, 15)._to_str_matrix()
    # maze = [''.join(str(x) for x in row[0:]) for row in maze]
    # maze[1] = change_char(maze[1], len(maze[1])-2, 'P')
    # maze[len(maze)-2] = change_char(maze[len(maze)-2], 1, '.')

    # context = {'map': maze}

    # print(maze)
    # args = pacman.readCommand( [ '-l', 'testMaze', '-p', 'SearchAgent', '-a', 'fn=astar', '-t'] ) # Get game components based on input
    # game = pacman.runGames( **args )
    # print pacman navigating through the maze 
    # for x in game[0]:
    #     print(x)
    # print('Average Score:', sum(game[1]) / float(len(game[1])))
    # print('Scores:       ', ', '.join([str(game[1]) for score in game[1]]))
    # print('Win Rate:      %d/%d (%.2f)' % (game[2].count(True), len(game[2]), game[3]))
    # print('Record:       ', ', '.join([ ['Loss', 'Win'][int(w)] for w in game[2]]))
    return render(request, 'webgraph/landing.html')


def generateMaze(request):
    if request.method == 'POST':
        maze = Maze.generate(30, 15)._to_str_matrix()
        maze = [''.join(str(x) for x in row[0:]) for row in maze]
        maze[1] = change_char(maze[1], len(maze[1])-2, 'P')
        maze[len(maze)-2] = change_char(maze[len(maze)-2], 1, '.')
        return JsonResponse({'maze': maze})
    else:
        return JsonResponse({'maze': []})

def runPacman(request):
    print("called runPacman")
    if request.method == 'POST':
        data_json = request.body
        data = data_json.decode("utf-8").replace('alg=','').split('&')
        alg = data[0]
        del data[0] # data = maze layout
        # print(alg)
        for i in range(len(data)):
            data[i] = data[i].replace('maze%5B%5D=', '').replace('%25', '%').replace('%20', ' ')
        # print(data)
        parameter = 'fn=' + alg
        args = pacman.readCommand( [ '-l', 'generateMaze', '-p', 'SearchAgent', '-a', parameter, '-t'], data ) # Get game components based on input
        game = pacman.runGames( **args )
        # for x in game[0]:
        #     print(x)
        return JsonResponse({'output': game[0]})
    else:
        return JsonResponse({'output': []})