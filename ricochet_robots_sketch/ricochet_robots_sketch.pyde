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
def setup():
    global grid, g_robot
    size(900, 900)
    background(120)
    translate(margin, margin)
    grid = Grid(n_tiles,n_tiles)
    grid.print_grid()
    
    
def draw():
    translate(margin, margin)
    grid.print_grid()
    '''grid.robots['blue'].move_robot(grid.grid, 'right', 0.1)
    grid.robots['green'].move_robot(grid.grid, 'up', 0.1)
    grid.robots['yellow'].move_robot(grid.grid, 'down', 0.1)
    grid.robots['red'].move_robot(grid.grid, 'left', 0.1)'''
    #g_robot.print_robot()
    #moving = g_robot.move_robot(grid.grid, 'up', 0.10)
    
    
