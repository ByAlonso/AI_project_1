class State():
    def __init__(self, robots):
        # self.grid_ = grid
        # self.grid = grid.grid
        self.robots = robots
        # self.goal = grid.new_goal
        self.action = ''
        self.is_goal = False
        
    def check_if_goal(self, goal):
        target_robot = self.robots[goal.clr_name ]
        self.is_goal = target_robot.x_pos == goal.x_pos and target_robot.y_pos == goal.y_pos
        # self.is_goal = any([[self.robots[robot].x_pos,self.robots[robot].y_pos,self.robots[robot].name] == [self.goal.x_pos,self.goal.y_pos,self.goal.clr_name] for robot in self.robots])
    
    def print_state(self):
        print("***********")
        for r in self.robots:
            print(r, self.robots[r].x_pos, self.robots[r].y_pos)
        print("ACTION:", self.action)
        # print("GOAL:",self.goal.x_pos,self.goal.y_pos)
        print("is_goal:", self.is_goal)
        print("***********")
    
    def set_actions(self,robot,dir):
        self.action = '{} {}'.format(robot,dir)
        
