#Import PyGame Zero Library
import pgzrun
import random

TITLE = "Good Shot Game"
WIDTH = 500
HEIGHT = 500

message = ""

alien = Actor("alien")
#alien.pos = (50, 50)

def draw():
    screen.clear()
    screen.fill("green")
    alien.draw()
    screen.draw.text(message, center = (350, 20), fontsize = 30)

def placealien():
    alien.x = random.randint(50, 450)
    alien.y = random.randint(50, 450)

def on_mouse_down(pos):
    global message
    if alien.collidepoint (pos):
        message = "Good Shot!"
        placealien()
    else: 
        message = "You Missed The Shot"
placealien()
    
#To Make The Windows Stay On Screen
pgzrun.go()
