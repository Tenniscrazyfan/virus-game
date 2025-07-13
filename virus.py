import pgzrun
import random
from time import time

WIDTH = 600
HEIGHT = 600

virus = Actor("samell_bacteria")
injection = Actor("flower")
human = Actor("alien")

score = 0
lives = 3  
virus.pos = 400, 400
injection.pos = 300, 300
human.pos = 250, 500
starttime = time()
totaltime = 0
game_over = False

def draw():
    screen.fill("sky blue")
    virus.draw()
    injection.draw()
    human.draw()

    screen.draw.text("Score: " + str(score), (10, 10), color="black")
    screen.draw.text("Lives: " + str(lives), (10, 30), color="black")

    if game_over:
        screen.fill("black")
        screen.draw.text("GAME OVER", center=(350,350), fontsize=60, color="white")
        screen.draw.text("Score: " + str(score), (10, 10), color="white")
        screen.draw.text("Lives: " + str(lives), (10, 30), color="white")

    

def update():
    global score, lives, game_over,starttime,totaltime

    
    totaltime = time() 

    if totaltime - starttime >= 1:
        starttime = time()
        virus.pos = random.randint(50, 550), random.randint(50, 550)
        
    
    if keyboard.left and human.x > 30:
        human.x = human.x - 2
    if keyboard.right and human.x < 570:
        human.x = human.x + 2
    if keyboard.up and human.y > 30:
        human.y = human.y - 2
    if keyboard.down and human.y < 570:
        human.y = human.y + 2

    
    if human.colliderect(virus):
        score = score - 10
        lives = lives - 1
        virus.pos = random.randint(50, 550), random.randint(50, 550)
        if lives <= 0:
            game_over = True

    
    if human.colliderect(injection):
        score = score + 11
        injection.pos = random.randint(50, 550), random.randint(50, 550)




pgzrun.go()






   



