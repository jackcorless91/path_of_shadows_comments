import os
# imports os module to help interact with the operating system, it is used to clear the next frame

import time
# imports time module, used to pause for a specified amount of time

import random
# imports random module, generates a random number


width = 20
height = 10
balls = ['O', '●', '•']
ball_count = 5

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

    """
    clears screen to prepare for upcoming frame
    """

positions = [(random.randint(0, width-1), random.randint(0, height-1)) for _ in range(ball_count)]

    """
    updates a new list of random positions for the balls to be on in the next frame
    """

while True:
    clear_screen()
    for y in range(height):
        for x in range(width):
            if (x, y) in positions:
                print(random.choice(balls), end='')
            else:
                print(' ', end='')

                """
                checks if x and y positions are a ball, if it is print a ball symbol
                """
        print()
    time.sleep(0.5)

    """
    pauses for 0.5 seconds before reiterating
    """
    positions = [(random.randint(0, width-1), random.randint(0, height-1)) for _ in range(ball_count)]

    """
    while true constantly iterating through the loop and refreshing the screen 
    
    this program continuously updates each frame to put 5 randomly placed balls on the screen, after each frame the next is cleared and updated creating an animation of balls bouncing around the screen
    """