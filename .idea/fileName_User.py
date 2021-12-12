# Get the maze file's filename from the user:
import os,sys
def user_input():
    filename = ''
    while True:
        print('Enter the filename of the maze (or LIST or QUIT):')
        filename = input('> ')
    # List all the maze files in the current folder:
        if filename.upper() == 'LIST':
            print('Maze files found in', os.getcwd())
            for fileInCurrentFolder in os.listdir():
                if (fileInCurrentFolder.startswith('maze') and
                    fileInCurrentFolder.endswith('.txt')):
                        print(' ', fileInCurrentFolder)
            continue
        if filename.upper() == 'QUIT':
            sys.exit()
        if os.path.exists(filename):
            break
        print('There is no file named', filename)
    return filename