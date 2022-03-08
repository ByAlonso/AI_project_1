from grid import Grid
from robot import Robot
from bfs import BFS
import time

n_tiles = 16
margin = 50
global selected_robot
def setup():
    global grid, g_robot
    size(800, 800)
    background(120)
    grid = Grid(n_tiles,n_tiles)
    grid.print_grid()
    bfs = BFS(grid)
    current_node = bfs.generate_tree()
    current_node.state.print_state()
    actions = []
    actions.append(current_node.state.action)
    while current_node.parent != None:
        current_node = current_node.parent
        actions.append(current_node.state.action)
    actions.reverse()
    print(actions)
    
    
def draw():
    grid.print_grid()
    
def mouseClicked():
    global selected_robot
    x_coord = mouseX // 50
    y_coord = mouseY //50
    selected_robot = grid.select_robot(x_coord,y_coord)
        
def keyPressed():  
    global selected_robot  
    if selected_robot:
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
        grid.check_goal(selected_robot)
