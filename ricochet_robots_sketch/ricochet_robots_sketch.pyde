from grid import Grid
from robot import Robot
from bfs import BFS
from dfs import DFS
from a_star import AStar
import time

from KThread import KThread

n_tiles = 16
margin = 50

# AI
n = 1 
step = 0
algo = 'bfs'

# Gameplay
results = {}
best = []
selected_robot = None
num_moves = ''
wait_time = 30

global path, methods
def setup():
    global grid, g_robot, path, dfs, methods
    size(800, 1000)
    background(120)
    grid = Grid(n_tiles,n_tiles)
    grid.print_grid()
    
    methods = {'dfs': DFS(grid, 20),
               'bfs': BFS(grid),
               'a_star': AStar(grid)}
        
    

t0 = 0
my_thread = None
start_timer = 0
def draw():
    global n, path, step, results, t0, my_thread, start_timer, best
    
    background(120)
    grid.print_grid()
    if grid.new_goal:
        textSize(50)
        text('Goal:', 20, 890);
        grid.new_goal.print_goal(3, 17)
    
    if step == 0:
        results = {}
        # Set goal and start threads
        methods[algo].set_goal(grid.new_goal, grid.robots)
        # Thread
        my_thread = KThread(target=methods[algo].th_search, args = (grid.robots, results))
        
        t0 = time.time()
        my_thread.start()
        step += 1
        print('Click on the game and write the number of moves + enter')
        start_timer = time.time()
    
    elif step == 1:
        if not results:
            start_timer = time.time()
        else:
            best = sorted(results.items(), key=lambda item: item[1][0])
            print_plays(best)
                
            time_remaining = round(wait_time - (time.time() - start_timer))
            if time_remaining > 0:
                textSize(100)
                text(str(time_remaining), 550, 900); 
                if len(results) >= 2:
                    start_timer = 0
            else:
                # TODO: Kill Threads
                if my_thread.isAlive():
                    my_thread.terminate()
                path = best[0][1][1]
                path = path[::-1] if path != None else None
                step += 2 if best[0][0] == 'player' else 1
                print(best[0])
                
        
    elif step == 2:
        print_plays(best)
        # AI plays
        if path != None and n < len(path):
            col, dir = path[n].split(' ')
            if not grid.robots[col].move_robot(grid.grid, dir, grid.robots, 0.1):
                n += 1
        elif path == None:
            print('Algorithm did not find path')
        else:
            arrived = grid.check_goal(grid.robots[grid.new_goal.clr_name])
            step, n = (0, 1) if arrived == True and grid.new_goal else (4, n)
    
    elif step == 3:
        print_plays(best)
        # Player plays
        player_goal = grid.check_goal(grid.robots[grid.new_goal.clr_name])
        if player_goal:
            grid.select_robot(7,7)
            step = 0 if grid.new_goal else 4
            
        
    elif step == 4:
        print('End of game')
        step = 5

        
def mouseClicked():
    global selected_robot, step
    x_coord = mouseX // 50
    y_coord = mouseY //50
    if step == 3:
        selected_robot = grid.select_robot(x_coord,y_coord)
        
def keyPressed():  
    global selected_robot, step, num_moves, results
    if step == 1:
        if key.isnumeric():
            num_moves += key
        elif key == '\n':
            results['player'] = (int(num_moves), [])
            num_moves = ''
            
        
    
    if selected_robot and step == 3:
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
        # grid.check_goal(selected_robot)

def print_plays(best):
    for i, (k, v) in enumerate(best):
        textSize(25)
        text('{}: {} moves'.format(k, v[0]), 300, 840 + 25*i);
