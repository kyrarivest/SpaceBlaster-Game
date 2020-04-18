"""Kyra Rivest
Python Space Blasters Game
Mr. Rossetti
20 Jan. 2019"""

from graphics import *
from time import sleep

step = 10
win = GraphWin("Space Game", 800,600)
background = Image(Point(400,300), "newspace.PPM")
background.draw(win)

home = Point(400,530)
rocket = Image(home, "ship2.PPM")
rocket.draw(win)

key = ""
laser_active = False

#moves the rockets laser
def move_laser():
    if (laser.getCenter().getY() > 0):
        laser.move(0,-10)
        sleep(0.09)
        return True
    else:
        laser.undraw()
        return False

#main loop
while (key != "Q"):
    key = win.checkKey().upper()
    if laser_active:
        laser_active = move_laser()
    
    if (key=="LEFT"):
        if rocket.getAnchor().getX()> 40:
            rocket.move(-1*step,0)

    elif(key == "RIGHT"):
        if rocket.getAnchor().getX() < 760:
            rocket.move(step,0)

    elif (key == "SPACE" and not laser_active):
        laser = Circle(rocket.getAnchor(), 6)
        laser.setFill("red")
        laser.draw(win)
        laser_active = True

print("exiting...")
sleep(2)
win.close()


