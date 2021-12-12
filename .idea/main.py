# Maze file constants:
WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'

PLAYER = '@'  # (!) Try changing this to '+' or 'o'.
BLOCK = chr(9617)  # Character 9617 is '░'

from display_file import *
from fileName_User import *

print("**************Maze Runner**************")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

filename = user_input()

# Load the maze from a file:
mazeFile = open(filename)
maze = {}
lines = mazeFile.readlines()
playerx = None
playery = None
exitx = None
exity = None
y = 0
WIDTH = 0

for line in lines:
    WIDTH = len(line.rstrip())
    for x, character in enumerate(line.rstrip()):
        assert character in (WALL, EMPTY, START, EXIT), 'Invalid character at column {}, line {}'.format(x + 1, y + 1)
        if character in (WALL, EMPTY):
            maze[(x, y)] = character
        elif character == START:
            playerx, playery = x, y
            maze[(x, y)] = EMPTY
        elif character == EXIT:
            exitx, exity = x, y
            maze[(x, y)] = EMPTY
    y += 1
HEIGHT = y

assert playerx is not None and playery is not None, 'No start in maze file.'
assert exitx is not None and exity is not None, 'No exit in maze file.'

while True:
    displayMaze(maze,HEIGHT,WIDTH,playerx,playery,PLAYER,BLOCK,WALL,exitx,exity)

    while True:
        #GameMaze(playerx,playery,EMPTY,exitx,exity,WALL,maze,HEIGHT, WIDTH,PLAYER, BLOCK)
        print('                           W')
        print('Enter direction, or QUIT: ASD')
        move = input('> ').upper()
        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if move not in ['W', 'A', 'S', 'D']:
            print('Invalid direction. Enter one of W, A, S, or D.')
            continue

        # Check if the player can move in that direction:
        if move == 'W' and maze[(playerx, playery - 1)] == EMPTY:
            break
        elif move == 'S' and maze[(playerx, playery + 1)] == EMPTY:
            break
        elif move == 'A' and maze[(playerx - 1, playery)] == EMPTY:
            break
        elif move == 'D' and maze[(playerx + 1, playery)] == EMPTY:
            break

        print('You cannot move in that direction.')
        # Keep moving in this direction until you encounter a branch point.
    if move == 'W':
        while True:
            playery -= 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx, playery - 1)] == WALL:
                break  # Break if we've hit a wall.
            if (maze[(playerx - 1, playery)] == EMPTY or maze[(playerx + 1, playery)] == EMPTY):
                break  # Break if we've reached a branch point.
    elif move == 'S':
        while True:
            playery += 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx, playery + 1)] == WALL:
                break  # Break if we've hit a wall.
            if (maze[(playerx - 1, playery)] == EMPTY or maze[(playerx + 1, playery)] == EMPTY):
                break  # Break if we've reached a branch point.
    elif move == 'A':
        while True:
            playerx -= 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx - 1, playery)] == WALL:
                break  # Break if we've hit a wall.
            if (maze[(playerx, playery - 1)] == EMPTY or maze[(playerx, playery + 1)] == EMPTY):
                break  # Break if we've reached a branch point.
    elif move == 'D':
        while True:
            playerx += 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx + 1, playery)] == WALL:
                break  # Break if we've hit a wall.
            if (maze[(playerx, playery - 1)] == EMPTY or maze[(playerx, playery + 1)] == EMPTY):
                break  # Break if we've reached a branch point.

    if (playerx, playery) == (exitx, exity):
        displayMaze(maze, HEIGHT, WIDTH, playerx, playery, PLAYER, BLOCK, WALL, exitx, exity)
        print('You have reached the exit! Good job!')
        print('Thanks for playing!')
        sys.exit()