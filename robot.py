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
    # Clear console screen using ANSI escape codes
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()

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

bot()
