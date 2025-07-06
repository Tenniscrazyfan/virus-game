import pgzrun
import random
import time

WIDTH = 600
HEIGHT = 600

virus = Actor("bee")
injection = Actor("flower")
human = Actor("alien")
score = 0
endgame = False
life = 3

virus.pos = 400,400
injection.pos = 300,300
human.pos = 250,500

def draw():
    screen.fill("Sky Blue")
    virus.draw()
    injection.draw()
    human.draw()

def update():
    global virus_attack,score,life

    if keyboard.left and human.x > 20:
        human.x = human.x - 5
    if keyboard.right and human.x < 570:
        human.x = human.x + 5
    if keyboard.up and human.y > 20:
        human.y = human.y - 5
    if keyboard.down and human.y < 570:
        human.y = human.y + 5

    for i in range(5):
        virus.x = random.randint(50,550)
        virus.y = random.randint(50,550)
        injection.x = random.randint(50,550)
        injection.y = random.randint(50,550)
        time.sleep(1)

    if human.colliderect(virus):
        score = score - 10
        life = life - 1
    if human.colliderect(injection):
        score = score + 11




   

pgzrun.go()

