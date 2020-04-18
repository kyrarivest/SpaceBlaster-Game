"""Kyra Rivest
Python Space Blasters Game
Mr. Rossetti
20 Jan. 2019"""

from graphics import *
from time import sleep
from random import randrange

step = 10
win = GraphWin("Space Game", 800,600)
background = Image(Point(400,300), "newspace.PPM")
background.draw(win)

home = Point(400,530)
rocket = Image(home, "ship2.PPM")
rocket.draw(win)


key = ""
laser_active = False
enemy_active = False
enemy_laseractive = False

#moves the rockets laser
def move_laser():
    if (laser.getCenter().getY() > 0):
        laser.move(0,-10)
        sleep(0.009)
        return True
    else:
        laser.undraw()
        return False

#moves enemy laser
def move_enemylaser():
    if(enemy_laser.getCenter().getY() < 600):
        enemy_laser.move(0,10)
        sleep(.09)
        return True
    else:
        enemy_laser.undraw()
        return False

#moves enemy
def enemy_move(): 
    if x == 730:
        if (enemy.getAnchor().getX() + 38) > 0:
            enemy.move(-10,0)
            sleep(.09)
            return True
        else:
            enemy.undraw()
            return False
    elif x == 30:
        if (enemy.getAnchor().getX() - 38) < 800:
            enemy.move(10,0)
            sleep(.09)
            return True
        else:
            enemy.undraw()
            return False

#determines what side enemy starts on
def enemyStart():
    dir = randrange(1,3)
    if dir == 1:
        return 730
    else:
        return 30
   

    
#main loop
while (key != "Q"):
    key = win.checkKey().upper()
    
    #defines and moves enemy
    freq = randrange(1,1001)
    if(not(enemy_active) and (freq == 1)):
        enemy_active = True
        y = randrange(75,200)
        x = enemyStart()
        enemy = Image(Point(x,y), "enemyShip.PPM")
        enemy.draw(win)
        
    elif enemy_active:
        enemy_active = enemy_move()

    #fires enemy laser
    if enemy_active:
        if not enemy_laseractive and enemy.getAnchor().getX() < (rocket.getAnchor().getX() + 20) and enemy.getAnchor().getX() > (rocket.getAnchor().getX() - 20):
            enemy_laser = Circle(enemy.getAnchor(), 6)
            enemy_laser.setFill("blue")
            enemy_laser.draw(win)
            enemy_laseractive = True
        
        elif enemy_laseractive:
            enemy_laseractive = move_enemylaser()

    #rocket code    
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


