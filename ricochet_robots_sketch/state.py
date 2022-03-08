class State():
    def __init__(self,grid):
        self.grid_ = grid
        self.grid = grid.grid
        self.robots = grid.robots
        self.goal = grid.new_goal
        self.action = [None,None]
        self.is_goal = self.check_if_goal()
        
    def check_if_goal(self):
        self.is_goal = any([[self.robots[robot].x_pos,self.robots[robot].y_pos,self.robots[robot].name] == [self.goal.x_pos,self.goal.y_pos,self.goal.clr_name] for robot in self.robots])
    
    def print_state(self):
        print("***********")
        for r in self.robots:
            print(r, self.robots[r].x_pos, self.robots[r].y_pos)
        print("ACTION:", self.action[0],self.action[1])
        print("GOAL:",self.goal.x_pos,self.goal.y_pos)
        print("is_goal:", self.is_goal)
        print("***********")
    
    def set_actions(self,robot,dir):
        self.action = [robot,dir]
        
