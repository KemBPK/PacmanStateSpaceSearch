from django.urls import path
from . import views

urlpatterns = [
    #path('', views.testpage, name="testpage"),
    path('', views.landing, name='landing'),
    path('runPacman', views.runPacman, name='runPacman'),
    path('generateMaze', views.generateMaze, name="generateMaze")
]