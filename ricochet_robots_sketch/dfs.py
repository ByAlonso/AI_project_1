from copy import deepcopy
    
class DFS():
    def __init__(self, grid, max_n):
        self.board = deepcopy(grid.grid)
        self.max_n = max_n
                
        # Possible actions and robots
        self.actions = ['up','left','down','right']
        self.robot_clr = ['green','blue','yellow','red']
                        

    def set_goal(self, goal, robots):
        self.goal_clr = goal.clr_name
        self.goal_x = goal.x_pos
        self.goal_y = goal.y_pos
        
        # Optimize robot order
        i = self.robot_clr.index(self.goal_clr)
        self.robot_clr.pop(i)
        dists = {self.robot_clr[0]:(robots[self.robot_clr[0]].x_pos**2 + robots[self.robot_clr[0]].y_pos**2),
                 self.robot_clr[1]:(robots[self.robot_clr[1]].x_pos**2 + robots[self.robot_clr[1]].y_pos**2),
                 self.robot_clr[2]:(robots[self.robot_clr[2]].x_pos**2 + robots[self.robot_clr[2]].y_pos**2)}
        self.robot_clr = [k for k, v in sorted(dists.items(), key=lambda item: item[1], reverse=True)]
        self.robot_clr.insert(0, self.goal_clr)
                
                                
    def search(self, robots, action = '', n = 0):       
        # Create the state as a copy of the robots
        state = deepcopy(robots)
                
        # If n > max_n retun None
        if n > self.max_n:
            return None
        
        # Do action
        self.move_robot(state, action)
        
        # If is goal return [action]
        if self.check_goal(state):
            return [action]
        
        # For every possible action run search
            # If it returns != None -> return append(action)
        movements = self.possible_movements(state, action)
        for mov in movements:
            # print(mov)
            res = self.search(state, mov, n+1)
            if res != None:
                res.append(action)
                return res
            
        return None
        
    
    def move_robot(self, robots, action):
        if action != '':
            col, dir = action.split(' ')
            while robots[col].move_robot(self.board,dir, robots):
                pass
        
    def check_goal(self,robots):
        robot = robots[self.goal_clr]
        if robot.x_pos == self.goal_x and robot.y_pos == self.goal_y:
            return True
        else:
            return False

    def possible_movements(self, robots, last_action):
        movements = []
        for robot in self.robot_clr:
            for dir in self.actions:
                mov = '{} {}'.format(robot, dir)
                if mov != last_action and robots[robot].can_move(self.board, dir, robots):
                    movements.append(mov)
        return movements
        
    
    
    
    
