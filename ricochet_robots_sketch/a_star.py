import copy

class AStar():
    def __init__(self,grid):
        self.grid = copy.deepcopy(grid.grid)
        self.actions = ['up','left','down','right']
        self.robot_clr = ['green','blue','yellow','red']
    
    def set_goal(self, goal, robots):
        self.goal = goal
        
        self.heuristics = self.compute_heuristic(goal)
    
        
    
    def search(self, robots):
        # Do Search
        return None
    
    

    # Pre-compute heuristic for every tile given goal
    def compute_heuristic(self, goal, grid_size=16):
        goal_x = goal.x_pos
        goal_y = goal.y_pos
        
        empty_grid = [[-1 for x in range(grid_size)] for y in range(grid_size)]
        empty_grid[goal_y][goal_x] = 0
        
        # Middle Part
        empty_grid[7][7] = 0
        empty_grid[7][8] = 0
        empty_grid[8][7] = 0
        empty_grid[8][8] = 0

        still_neg = True
        v = 0
        print(goal_x, goal_y)
        while still_neg:
            still_neg = False
            for i in range(grid_size):
                for j in range(grid_size):
                    if still_neg == False and empty_grid[i][j] == -1:
                        still_neg = True
                    if empty_grid[i][j] == v:
                        for dir in self.actions:
                            step = 1 if dir == 'right' or dir == 'down' else -1
                            y, x = i, j
                            while 0 <= y <= 15 and 0 <= x <= 15:
                                # Check for walls
                                if dir == 'right':
                                    if self.grid[y][x].has_right_wall:
                                        break
                                    x += 1 
                                elif dir == 'down':
                                    if self.grid[y][x].has_down_wall:
                                        break
                                    y += 1
                                elif dir == 'left':
                                    if self.grid[y][x].has_left_wall:
                                        break
                                    x -= 1 
                                else:
                                    if self.grid[y][x].has_up_wall:
                                        break
                                    y -= 1
                                
                                if x < 0 or x > 15 or y < 0 or y > 15:
                                    break

                                if empty_grid[y][x] == -1:
                                    empty_grid[y][x] = v + 1
            v += 1
        return empty_grid
