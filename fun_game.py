import os
import time
import random

width = 20
height = 10
balls = ['O', '●', '•']
ball_count = 5

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

positions = [(random.randint(0, width-1), random.randint(0, height-1)) for _ in range(ball_count)]

while True:
    clear_screen()
    for y in range(height):
        for x in range(width):
            if (x, y) in positions:
                print(random.choice(balls), end='')
            else:
                print(' ', end='')
        print()
    time.sleep(0.5)
    positions = [(random.randint(0, width-1), random.randint(0, height-1)) for _ in range(ball_count)]
