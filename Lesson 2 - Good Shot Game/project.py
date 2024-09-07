#Import PyGame Zero Library
import pgzrun
import random

TITLE = "Good Shot Game"
WIDTH = 500
HEIGHT = 500

message = ""

frog = Actor("frog")
#frog.pos = (50, 50)

def draw():
    screen.clear()
    screen.fill("green")
    frog.draw()
    screen.draw.text(message, center = (350, 20), fontsize = 30)

def placefrog():
    frog.x = random.randint(50, 450)
    frog.y = random.randint(50, 450)

def on_mouse_down(pos):
    global message
    if frog.collidepoint (pos):
        message = "Good Shot!"
        placefrog()
    else: 
        message = "You Missed The Shot"
placefrog()
    
#To Make The Windows Stay On Screen
pgzrun.go()
