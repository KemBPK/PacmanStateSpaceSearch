# PacmanStateSpaceSearch
<br>
CPSC 481

Brandon Kem (leader)<br>
Antonio Guzman<br>
Ye Lim Koo<br>

# Contribution
<br>

* http://ai.berkeley.edu/project_overview.html

<br>
The code for map generation is provided by: <br>

* https://github.com/boppreh/maze

# External library
<br>

* django

* pytz

# Setup Instruction
<br>

* Download latest Python

* Clone repo into your computer and nagivate to /pacmanstatespacesearch/ folder inside the terminal

* Then execute the following commands:
    ```
    python -m venv venv               //This will create a virtual environment to run the app
    venv\Scripts\activate             //This will run a virtual environment
    pip install django                //This will install the django packet
    pip install pytz                  //This should already be installed 

    ```
    
* Other commands:

    ```
     deactivate                        //This will exit the virtual environment
     ```

# Running the website
<br>

* Use the following commands in the terminal:

    ```
    venv\Scripts\activate             //This will run a virtual environment
    python manage.py runserver        //This will run the website in localhost
    ```
    
* Then type in the URL http://localhost:8000 to test the website.

# Functional Description
<br>

    ```
    .ebextension
        django.config       - specifies file path for AWS to run the website

    .elasticbeanstalk
        config.yml          - specifies django configuration for AWS

    pacmanModule
        layout folder       - contains maps (only used for testing)
        game.py             - contains the code to configure the pacman game
        ghostAgents.py      - contains the code for ghosts (needed for compiling) 
        graphicsDisplay.py  - contains the code for the graphic display (used for testing)
        graphicsUtils.py    - contains the code for the graphic display 
        layout.py           - contains the code to import the pacman into the game
        maze.py             - contains the code for generating the pacman map
        pacman.py           - contains the code for running the pacman game
        pacmanAgent.py      - contains example of pacman configurations (not used in this project)
        search.py           - contains the code for the search algorithms 
        searchAgents.py     - contains the code for configuring pacman
        textDisplay.py      - contains the code to display the graphics in text
        util.py             - contains important data structures and functions
    
    pacmanstatespacesearch
        settings.py         - settings for the website
        urls.py             - import urls from the webgraph app
        wsgi.py             - runs some code before starting the servers

    static
        css
            landing.css     - contains custom css for the website's design

    templates
        webgraph
            landing.html    - main html page for the website
        base.html           - a layout for all html page

    webgraph
        apps.py             - configures app
        urls.py             - configure url for app 
        views.py            - contains backend code for the website
    
    manage.py               - contains code to run the webserver
    requirement.txt         - a text file that specifies what library to install

    ```