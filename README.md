# Hex Game
Hex is a 2-player board game played on a rhombus/parallelogram board tiled
with hexagons. Each player is assigned opposite colored edges and the
objective is to create a continuous link that connects the two sides marked
by the player’s color. More information about the game is found here: http://www.ludoteka.com/hex-en.html 

## Video Presentation
  [![Watch the video](https://img.youtube.com/vi/pweQzGeLW1o/0.jpg)](https://youtu.be/pweQzGeLW1o)

## System Installation
  1. Python>3.7
  2. Download any python virtual environment manager e.i. [pipenv (recommended)](https://pypi.org/project/pipenv/), [virtualenv](https://virtualenv.pypa.io/en/latest/), [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), [conda](https://docs.conda.io/en/latest/)

## Project Installation
#### Pipenv
  1. `pipenv install`
#### Virtualenv, Virtualenvwrapper
  1. `python3 -m venv [environment-name]`
  2. `source [environment-name]/bin/activate`
  3. `pip install pygame`
  
## Running the Project
#### Pipenv
  1. `pipenv shell`
  2. `python hex.py`
#### Virtualenv, Virtualenvwrapper
  1. `source [environment-name]/bin/activate`
  2. `python hex.py`

## Library Used
  * [Pygame](https://www.pygame.org/news)

## Resources
  * [A* Pathfinding](https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2)
  * [Class Based Pygame](http://pygametutorials.wikidot.com/tutorials-basic)
