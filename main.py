import random

import pgzrun

from pgzhelper import *

WIDTH = 1000
HEIGHT = 800

zombie_run = [
    'zombie/run/tile002',
    'zombie/run/tile003',
    'zombie/run/tile004',
    'zombie/run/tile005',
]

zombie_die = [
    'zombie/die/tile014',
    'zombie/die/tile015',
    'zombie/die/tile016',
    'zombie/die/tile017',
    'zombie/die/tile018',
    'zombie/die/tile019',
    'zombie/die/tile020',
    'zombie/die/tile021',
    'zombie/die/tile022',
    'zombie/die/tile023',
    'zombie/die/tile024',
]

witch_idle = [
    'witch/idle/tile000',
    'witch/idle/tile001',
    'witch/idle/tile002',
    'witch/idle/tile003',
    'witch/idle/tile004',
    'witch/idle/tile005',
    'witch/idle/tile006',
    'witch/idle/tile007',
    'witch/idle/tile008',
    'witch/idle/tile009',
]

witch_attack = [
    'witch/attack/tile000',
    'witch/attack/tile001',
    'witch/attack/tile002',
    'witch/attack/tile003',
    'witch/attack/tile004',
    'witch/attack/tile005',
    'witch/attack/tile006',
    'witch/attack/tile007',
    'witch/attack/tile008',
    'witch/attack/tile009',
    'witch/attack/tile010',
    'witch/attack/tile011',
    'witch/attack/tile012',
]

zombie = Actor(zombie_run[0])
zombie.images = zombie_run

zombie.scale = 6
zombie.right = WIDTH + 80
zombie.bottom = HEIGHT - 20
zombie.fps = 5

witch = Actor(witch_idle[0])
witch.images = witch_idle

witch.scale = 3
witch.left = -130
witch.bottom = HEIGHT + 100
witch.fps = 7

questionBank = ['question', 'exam', 'quiz', 'mid term']
question = random.choice(questionBank)
typed = ''


def update():
    global typed, question
    zombie.animate()
    witch.animate()
    if witch_attack[-1] == witch.image:
        witch.images = witch_idle
        witch.left = -130
    if zombie.image == zombie_die[-1]:
        zombie.images = zombie_run
        typed = ''
        question = random.choice(questionBank)


def on_key_down(key):
    global typed
    print(key)

    if key in range(97, 123):
        # print(chr(key))
        typed += chr(key)

    if key == 32:
        typed += ' '

    if key == 8:
        typed = typed[0:-1]

    if typed == question:
        witch.images = witch_attack
        zombie.images = zombie_die
        witch.right = zombie.left + 50


def draw():
    screen.clear()
    screen.draw.text(question, (20, 100), fontsize=60)
    screen.draw.text(typed, (20, 100), fontsize=60, color='orange')
    zombie.draw()
    witch.draw()


pgzrun.go()
