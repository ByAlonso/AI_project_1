class BFS():
    def __init__(self,grid):
        self.grid = grid.grid
        self.robots = grid.robots
        self.goal = grid.new_goal
        self.actions = ['up','left','down','right']
        
        
