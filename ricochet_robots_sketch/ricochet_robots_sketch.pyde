from grid import Grid
from robot import Robot
from bfs import BFS
from dfs import DFS
import time


n_tiles = 16
margin = 50
n = 1
run_AI = True
global selected_robot, path, dfs
def setup():
    global grid, g_robot, path, dfs
    size(800, 800)
    background(120)
    grid = Grid(n_tiles,n_tiles)
    grid.print_grid()
    delay(1000)
    
    # bfs = BFS(grid)
    # current_node = bfs.generate_tree()
    # current_node.state.print_state()
    # actions = []
    # actions.append(current_node.state.action)
    # while current_node.parent != None:
    #     current_node = current_node.parent
    #     actions.append(current_node.state.action)
    # actions.reverse()
    # print(actions)
    
    dfs = DFS(grid, 7)
    
    
    
def draw():
    global n, path, run_AI
    grid.print_grid()
    
    if run_AI:
        dfs.set_goal(grid.new_goal, grid.robots)
        path = dfs.search(grid.robots)
        path = path[::-1] if path != None else None
        print(path)
        run_AI = False
    
    if path != None and n < len(path):
        col, dir = path[n].split(' ')
        if not grid.robots[col].move_robot(grid.grid, dir, grid.robots, 0.1):
            n += 1
        
    
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
