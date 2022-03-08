class State():
    def __init__(self,grid):
        self.grid = grid.grid
        self.robots = grid.robots
        self.goal = grid.new_goal
        self.action = None
        self.is_goal = self.check_if_goal()
        
    def check_if_goal(self):
        return any([[robot.x_pos,robot.y_pos,robot.name] == [self.goal.x_pos,self.goal.y_pos,self.goal.clr] for robot in self.robots])
        
