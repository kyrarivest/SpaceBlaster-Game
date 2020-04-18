"""Kyra Rivest
Python Space Blasters Game
Mr. Rossetti
20 Jan. 2019"""

from graphics import *
from time import sleep
from random import randrange

lives = 4
score = 100

def update_score(new_score):
    score_number.undraw()
    score_number = str(new_score)
    score_number.draw(win)
    

step = 10
win = GraphWin("Space Game", 800,600)
background = Image(Point(400,300), "newspace.PPM")
background.draw(win)

home = Point(400,530)
rocket = Image(home, "ship2.PPM")
rocket.draw(win)
   
score_label = Text(Point(500,20), "score: ")
score_label.setTextColor("light blue")
score_label.setSize(18)
score_label.draw(win)

score_number = Text(Point(550,20), str(score))
score_number.setTextColor("light blue")
score_number.setSize(18)
score_number.draw(win)

liveslabel = Text(Point(650,20), "Lives")
liveslabel.setSize(18)
liveslabel.setTextColor("red")
liveslabel.draw(win)

life1 = Rectangle(Point(680,10), Point(700,30))
life1.setFill("red")
life1.draw(win)

life2 = Rectangle(Point(710,10), Point(730,30))
life2.setFill("red")
life2.draw(win)


key = ""
laser_active = False
enemy_active = False
enemy_laseractive = False


#moves the rockets laser
def move_laser():
    if (laser.getCenter().getY() > 0):
        laser.move(0,-20)
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

def collison(target, object):
    x1 = target.getAnchor().getX() - (target.getWidth()/2)
    y1 = target.getAnchor().getY() - (target.getHeight()/2)
    x2 = target.getAnchor().getX() + (target.getWidth()/2)
    y2 = target.getAnchor().getY() + (target.getHeight()/2)

    laserX = object.getCenter().getX()
    laserY = object.getCenter().getY()

    if (laserX > x1 and laserX < x2 and laserY > y1 and laserY < y2):
        object.undraw()
        laser_active = False
        return True
    else:
        return False

    
def gameover_protocol(highscore):
    game_over = Text(Point(400,250), "GAME OVER")
    game_over.setTextColor("red")
    game_over.setSize(30)
    game_over.draw(win)

    score_label = Text(Point(380,310), "score: ")
    score_label.setTextColor("blue")
    score_label.setSize(24)
    score_label.draw(win)

    score_number = Text(Point(430,310), str(highscore))
    score_number.setTextColor("blue")
    score_number.setSize(24)
    score_number.draw(win)

    play_againBox = Rectangle(Point(200,350), Point(290,400))
    play_againBox.setFill("light blue")
    play_againBox.draw(win)
    play_againText = Text(play_againBox.getCenter(), "Play Again")
    play_againText.draw(win)

    quitBox = Rectangle(Point(500,350), Point(590,400))
    quitBox.setFill("light blue")
    quitBox.draw(win)
    quitText = Text(quitBox.getCenter(), "Quit")
    quitText.draw(win)

    click = win.getMouse()

    #play again
    if(click.getX() >200 and click.getX() <290 and click.getY() > 350 and click.getY() < 400):
        lives = 3
        score_label.undraw()
        score_number.undraw()
        game_over.undraw()
        play_againBox.undraw()
        play_againText.undraw()
        quitBox.undraw()
        quitText.undraw()

        rocket.draw(win)
        score_label = Text(Point(500,20), "score: ")
        score_label.setTextColor("light blue")
        score_label.setSize(18)
        score_label.draw(win)

        score = 100
        score_number = Text(Point(550,20), str(score))
        score_number.setTextColor("light blue")
        score_number.setSize(18)
        score_number.draw(win)

        liveslabel = Text(Point(650,20), "Lives")
        liveslabel.setSize(18)
        liveslabel.setTextColor("red")
        liveslabel.draw(win)

        life1 = Rectangle(Point(680,10), Point(700,30))
        life1.setFill("red")
        life1.draw(win)

        life2 = Rectangle(Point(710,10), Point(730,30))
        life2.setFill("red")
        life2.draw(win)

        
    elif(click.getX() >500 and click.getX() <590 and click.getY() > 350 and click.getY() < 400):
        win.close()


#main loop
while (key != "Q"):
    while (lives > 0):
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
                
        #if enemy is hit
        if enemy_active:
            if laser_active:
                if collison(enemy, laser):
                    laser.undraw()
                    enemy.undraw()
                    enemy_active = False
                    if enemy_laseractive:
                        enemy_laser.undraw()
                    score = score + 100
                    score_number.undraw()
                    score_number = Text(Point(550 ,20), str(score))
                    score_number.setTextColor("light blue")
                    score_number.setSize(18)
                    score_number.draw(win)
                    

        #if rocket is hit
        if enemy_laseractive:
            if collison(rocket, enemy_laser):
                lives -= 1
                rocket.undraw()
                enemy_laser.undraw()
                enemy_laseractive = False
                if lives == 3:
                    life1.undraw()
                elif lives == 2:
                    life2.undraw()
                else:
                    break
                sleep(1)
                rocket.draw(win)

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
    #game over protocol

    rocket.undraw()
    score_label.undraw()
    score_number.undraw()
    if enemy_active:
        enemy.undraw()

    gameover_protocol(score)
        

print("exiting...")
sleep(2)
win.close()


