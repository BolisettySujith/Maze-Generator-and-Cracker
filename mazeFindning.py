import turtle                    # import turtle library
import time
import sys
from collections import deque
from mazeGenerator import MazeGenerator
import time

# this is the class for the Maze
class Maze(turtle.Turtle):               # define a Maze class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            # the turtle shape
        self.color("white")             # colour of the turtle
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)

class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

grid = []

class MazeSolver:
    global grid
    wn = turtle.Screen()               # define the turtle screen
    wn.bgcolor("black")                # set the background colour
    wn.title("A BFS Maze Solving Program")
    wn.setup(1600,1024)                  # setup the dimensions of the working window

    # set up classes
    maze = Maze()
    red = Red()
    blue = Blue()
    green = Green()
    yellow = Yellow()

    # setup lists
    walls = []
    path = []
    visited = set()
    frontier = deque()
    solution = {}                           # solution dictionary
    MazeGrid = MazeGenerator()

    def setup_maze(self,grid):                          # define a function called setup_maze
        global start_x, start_y, end_x, end_y      # set up global variables for start and end locations
        for y in range(len(grid)):                 # read in the grid line by line
            # print(y)
            for x in range(len(grid[y])):          # read each cell in the line
                # print(x)
                character = grid[y][x]             # assign the varaible "character" the the x and y location od the grid
                # print(character)
                screen_x = -900 + (x * 24)         # move to the x location on the screen staring at -588
                screen_y = 488 - (y * 24)          # move to the y location of the screen starting at 288

                if character == "+":
                    self.maze.goto(screen_x, screen_y)         # move pen to the x and y locaion and
                    self.maze.stamp()                          # stamp a copy of the turtle on the screen
                    self.walls.append((screen_x, screen_y))    # add coordinate to walls list

                if character == " " or character == "e":
                    self.path.append((screen_x, screen_y))     # add " " and e to path list

                if character == "e":
                    self.green.color("purple")
                    self.green.goto(screen_x, screen_y)       # send green sprite to screen location
                    end_x, end_y = screen_x,screen_y     # assign end locations variables to end_x and end_y
                    self.green.stamp()
                    self.green.color("green")

                if character == "s":
                    start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                    self.red.goto(screen_x, screen_y)


    def endProgram(self):
        self.wn.exitonclick()
        sys.exit()

    def search(self,x,y):
        self.frontier.append((x, y))
        self.solution[x,y] = x,y

        while len(self.frontier) > 0:          # exit while loop when frontier queue equals zero
            time.sleep(0)
            x, y = self.frontier.popleft()     # pop next entry in the frontier queue an assign to x and y location

            if(x - 24, y) in self.path and (x - 24, y) not in self.visited:  # check the cell on the left
                cell = (x - 24, y)
                self.solution[cell] = x, y    # backtracking routine [cell] is the previous cell. x, y is the current cell
                self.frontier.append(cell)   # add cell to frontier list
                self.visited.add((x-24, y))  # add cell to visited list

            if (x, y - 24) in self.path and (x, y - 24) not in self.visited:  # check the cell down
                cell = (x, y - 24)
                self.solution[cell] = x, y
                self.frontier.append(cell)
                self.visited.add((x, y - 24))
                print(self.solution)

            if(x + 24, y) in self.path and (x + 24, y) not in self.visited:   # check the cell on the  right
                cell = (x + 24, y)
                self.solution[cell] = x, y
                self.frontier.append(cell)
                self.visited.add((x +24, y))

            if(x, y + 24) in self.path and (x, y + 24) not in self.visited:  # check the cell up
                cell = (x, y + 24)
                self.solution[cell] = x, y
                self.frontier.append(cell)
                self.visited.add((x, y + 24))
            self.blue.goto(x,y) # identify frontier cells
            self.blue.stamp()


    def backRoute(self,x, y):
        self.red.goto(x, y)
        self.red.stamp()
        while (x, y) != (start_x, start_y):    # stop loop when current cells == start cell
            self.red.goto(self.solution[x, y])        # move the yellow sprite to the key value of solution ()
            self.red.stamp()
            x, y = self.solution[x, y]               # "key value" now becomes the new key
    
    def Display_maze(self, output_grid):

        for elm in output_grid:
            print("".join(elm))
        

    # main program starts here ####
    def main(self):  
        start_time = time.time()
        self.grid = self.MazeGrid.main()
        setup_begin = time.time()
        self.setup_maze(self.grid)
        setup_end = time.time()
        time.sleep(3)
        search_begin = time.time()
        self.search(start_x,start_y)
        search_end = time.time()
        back_begin = time.time()
        self.backRoute(end_x, end_y)
        back_end = time.time()
        End_time = time.time()
        print("Setup time: ", setup_end - setup_begin)
        print("Searching time: ", search_end - search_begin)
        print("Backtracking time: ", back_end - back_begin)
        print("Total time: ", End_time - start_time)
        self.wn.exitonclick()

    def __init__(self):
        self.main()

solver = MazeSolver()