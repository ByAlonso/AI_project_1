from grid import Grid
from robot import Robot
import time
def spaceShip(x, y, w, clr):
    fill(clr)
    ellipse(x, y, w/2.8, w/1.2)
    ellipse(x, y+w/10, w/2, w/2)
    ellipse(x, y+w/3, w/2.5, w/5)

    stroke(153)
    fill(255)    



n_tiles = 16
margin = 50
global selected_robot
def setup():
    global grid, g_robot
    size(800, 800)
    background(120)
    grid = Grid(n_tiles,n_tiles)
    grid.print_grid()
    
    
def draw():
    grid.print_grid()
    '''grid.robots['blue'].move_robot(grid.grid, 'right', 0.1)
    grid.robots['green'].move_robot(grid.grid, 'up', 0.1)
    grid.robots['yellow'].move_robot(grid.grid, 'down', 0.1)
    grid.robots['red'].move_robot(grid.grid, 'left', 0.1)'''
    #g_robot.print_robot()
    #moving = g_robot.move_robot(grid.grid, 'up', 0.10)
    
def mouseClicked():
    global selected_robot
    x_coord = mouseX // 50
    y_coord = mouseY //50
    selected_robot = grid.select_robot(x_coord,y_coord)
    
def keyPressed():  
    global selected_robot  
    if selected_robot:
        print(keyCode)
        if keyCode == UP:
            while selected_robot.move_robot(grid.grid,'up',1):
                pass
        if keyCode == DOWN:
            while selected_robot.move_robot(grid.grid,'down',1):
                pass
        if keyCode == RIGHT:
            while selected_robot.move_robot(grid.grid,'right',1):
                pass
        if keyCode == LEFT:
            while selected_robot.move_robot(grid.grid,'left',1):
                pass
