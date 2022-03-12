from grid import Grid
from robot import Robot
from bfs import BFS
from dfs import DFS
import time


n_tiles = 16
margin = 50

# AI
n = 1
step = 0
algo = 'bfs'

selected_robot = None
global path, methods
def setup():
    global grid, g_robot, path, dfs, methods
    size(800, 800)
    background(120)
    grid = Grid(n_tiles,n_tiles)
    grid.print_grid()
    
    methods = {'dfs': DFS(grid, 20),
               'bfs': BFS(grid)}
        
    
    
def draw():
    global n, path, step
    grid.print_grid()
    
    if step == 0:
        methods[algo].set_goal(grid.new_goal, grid.robots)
        t0 = time.time()
        path = methods[algo].search(grid.robots)
        path = path[::-1] if path != None else None
        print(path, time.time()-t0)
        step = 1
    
    elif step == 1:
        if path != None and n < len(path):
            col, dir = path[n].split(' ')
            if not grid.robots[col].move_robot(grid.grid, dir, grid.robots, 0.1):
                n += 1
        else:
            arrived = grid.check_goal(grid.robots[grid.new_goal.clr_name])
            step, n = (0, 1) if arrived == True and grid.new_goal else (2, n)

    elif step == 2:
        print('End of game')
        step = 3    
    
def mouseClicked():
    global selected_robot
    x_coord = mouseX // 50
    y_coord = mouseY //50
    selected_robot = grid.select_robot(x_coord,y_coord)
        
def keyPressed():  
    global selected_robot  
    if selected_robot:
        if keyCode == UP:
            while selected_robot.move_robot(grid.grid,'up', grid.robots, 1):
                pass
        if keyCode == DOWN:
            while selected_robot.move_robot(grid.grid,'down', grid.robots, 1):
                pass
        if keyCode == RIGHT:
            while selected_robot.move_robot(grid.grid,'right', grid.robots, 1):
                pass
        if keyCode == LEFT:
            while selected_robot.move_robot(grid.grid,'left', grid.robots, 1):
                pass
        grid.check_goal(selected_robot)
