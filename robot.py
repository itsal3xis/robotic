import time

import numpy as np
import sys

class Bot:
    def __init__(self, engine, posX, posY):
        self.engine = engine
        self.directions = ['up', 'down', 'left', 'right']
        self.board = self.launch(posX, posY)
        self.robot_pos = [posX, posY]  # Initial position of the robot
        self.walls = []

    def move(self, direction):
        if self.engine == 'on' and direction in self.directions:
            # Store the current position
            old_pos = self.robot_pos.copy()

            # Update position based on direction
            if direction == 'up':
                new_pos = [old_pos[0] - 1, old_pos[1]]
            elif direction == 'down':
                new_pos = [old_pos[0] + 1, old_pos[1]]
            elif direction == 'left':
                new_pos = [old_pos[0], old_pos[1] - 1]
            elif direction == 'right':
                new_pos = [old_pos[0], old_pos[1] + 1]

            # Check if new position is within the boundaries and not a wall
            if self.is_within_boundaries(new_pos) and new_pos not in self.walls:
                self.robot_pos = new_pos

                # Replace the last position of the robot with '~'
                self.board[old_pos[0], old_pos[1]] = '~'

                # Update the board with the new position of the robot
                self.board[self.robot_pos[0], self.robot_pos[1]] = 'R'

        return self.board

    def place_wall(self, posX, posY):
        # Place a wall at the specified position
        if self.is_within_boundaries([posX, posY]):
            self.board[posX, posY] = '#'
            self.walls.append([posX, posY])

    def launch(self, posX, posY):
        char = '~'
        board = np.array(([char] * 324))
        board = np.reshape(board, (18, 18))
        spawn_point = 'R'
        robot_pos = [posX, posY]
        board[robot_pos[0], robot_pos[1]] = spawn_point
        return board

    def is_within_boundaries(self, pos):
        # Check if pos is within the boundaries of the board
        return 0 <= pos[0] < self.board.shape[0] and 0 <= pos[1] < self.board.shape[1]

def clear_console():
    # Print a sufficient number of empty lines to simulate clearing the console
    print("\n" * 100)


def bot():
    posX = 5  # Specify initial x-coordinate
    posY = 8  # Specify initial y-coordinate
    r1 = Bot('on', posX, posY)

    while True:
        clear_console()

        # Place walls
        print("---------------------------------")
        print("Instructions:")
        print("  - Enter 'w' to place a wall")
        print("  - Enter 'up', 'down', 'left', or 'right' to move the robot")
        print("  - Enter 'q' to quit")

        r1.place_wall(4, 8)
        r1.place_wall(5, 9)
        r1.place_wall(6, 8)

        print(r1.board)

        command = input("Enter command: ")

        if command == 'q':
            break
        elif command == 'w':
            wall_y = int(input("Enter wall's x-coordinate: "))
            wall_x = int(input("Enter wall's y-coordinate: "))
            r1.place_wall(wall_x, wall_y)
        else:
            r1.move(command)


def challengeBeta():
    clear_console()
    print("Welcome to the Beta Challenger!\n")
    print("Your challenge is to modify the code below to make the bot navigate to the goal position (marked as 'G').")
    print("You can modify the Bot class methods and add any additional functions you need.")
    print("Use the move() method to control the bot's movement.")
    print("Once you think your code is correct, type 'done' to test it.")
    print("-----------------------------------")
    time.sleep(10)
    print('Starting in 5 seconds...')
    time.sleep(5)

    # Initial bot position
    posX = 5
    posY = 8

    # Create bot instance
    r1 = Bot('on', posX, posY)

    # Define the goal position
    goal_pos = [0, 0]  # Change this to the desired goal position

    # Place goal position on the board
    r1.board[goal_pos[0], goal_pos[1]] = 'G'

    # Game loop
    while True:
        clear_console()

        # Print board and instructions
        print("---------------------------------")
        print("Instructions:")
        print("  - Modify the code to navigate the bot to the goal position (marked as 'G').")
        print("  - Type 'done' to test your code.")
        print("  - Hint: The bot name is r1")
        print("---------------------------------")
        print(r1.board)

        # Get user input
        code = input("Write your code here:\n")

        # Check if the user wants to test their code
        if code.strip().lower() == 'done':
            break

        # Execute user's code
        try:
            exec(code)
        except Exception as e:
            print("Error executing code:", e)

    # Move the bot according to the user's code
    try:
        exec(code)
    except Exception as e:
        print("Error executing code:", e)

    # Check if the bot reached the goal position
    if r1.robot_pos == goal_pos:
        clear_console()
        clear_console()
        print("Congratulations! Your code successfully navigated the bot to the goal position.")
        time.sleep(5)
        challenges()
    else:
        print("Oops! Your code didn't navigate the bot to the goal position. Try again.")



def challenges():
    clear_console()
    print("Welcome to the challenges section !\nHere you can select a challenge and try to complete it.")
    print("----------------------------------\nSelect a challenge:\n")
    selection = int(input("1: Beta Challenger\n>  "))
    while selection < 1 or selection > 1:
        selection = int(input("Please choose an existing challenge"))
    if selection == 1:
        challengeBeta()

challenges()
#bot()
