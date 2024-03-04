import numpy as np

def robot(boardSizeX, boardSizeY, robotPosX, robotPosY):

    boardSizeX = int(boardSizeX)
    boardSizeY = int(boardSizeY)

    boardMaxSize = 18

    if boardSizeX > boardMaxSize:
        boardSizeX = 18
    if boardSizeY > boardMaxSize:
        boardSizeY = 18

    if boardSizeX == 0:
        boardSizeX = 1
    if boardSizeY == 0:
        boardSizeY = 1



    char = "."
    board = np.array(([char] * (boardSizeX * boardSizeY)))
    board = np.reshape(board, (boardSizeX, boardSizeY))

    robotChar = 'R'
    board[robotPosY, robotPosX] = robotChar

    print(board)





myRobot = robot(18,18, 2, 4)
