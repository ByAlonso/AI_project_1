from copy import deepcopy
from tree import Node
    
class DFS():
    def __init__(self, grid, max_n):
        self.board = deepcopy(grid.grid)
        self.max_n = max_n
                
        # Possible actions and robots
        self.actions = ['up','left','down','right']
        self.robot_clr = ['green','blue','yellow','red']
        
        self.visited = []
                        

    def set_goal(self, goal, robots):
        self.goal_clr = goal.clr_name
        self.goal_x = goal.x_pos
        self.goal_y = goal.y_pos
        
        self.visited = []
        
        # Optimize robot order
        i = self.robot_clr.index(self.goal_clr)
        self.robot_clr.pop(i)
        dists = {self.robot_clr[0]:((robots[self.robot_clr[0]].x_pos - self.goal_x)**2 + (robots[self.robot_clr[0]].y_pos - self.goal_y)**2),
                 self.robot_clr[1]:((robots[self.robot_clr[1]].x_pos - self.goal_x)**2 + (robots[self.robot_clr[1]].y_pos - self.goal_y)**2),
                 self.robot_clr[2]:((robots[self.robot_clr[2]].x_pos - self.goal_x)**2 + (robots[self.robot_clr[2]].y_pos - self.goal_y)**2)}
        self.robot_clr = [k for k, v in sorted(dists.items(), key=lambda item: item[1])]
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
    
        # See if state was already visited
        id = self.def_id(state, self.goal_clr)
        if id in self.visited:
            return None
        else:
            self.visited.append(id)

        
        # For every possible action run search
            # If it returns != None -> return append(action)
        movements = self.possible_movements(state)
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
            while robots[col].move_robot(self.board, dir, robots):
                pass
        
    def check_goal(self,robots):
        robot = robots[self.goal_clr]
        if robot.x_pos == self.goal_x and robot.y_pos == self.goal_y:
            return True
        else:
            return False

    def possible_movements(self, robots):
        movements = []
        for robot in self.robot_clr:
            for dir in self.actions:
                mov = '{} {}'.format(robot, dir)
                if robots[robot].can_move(self.board, dir, robots):
                    movements.append(mov)
        return movements
        
    # Define ID to easily compare if this state was already visited
    def def_id(self, robots, focus):
        g = 'g' if focus == None or focus == 'green' else 'd'
        b = 'b' if focus == None or focus == 'blue' else 'd'
        y = 'y' if focus == None or focus == 'yellow' else 'd'
        r = 'r' if focus == None or focus == 'red' else 'd'
        id = '{}{:02d}{:02d}{}{:02d}{:02d}{}{:02d}{:02d}{}{:02d}{:02d}'.format(
                                               g, robots['green'].x_pos, robots['green'].y_pos,
                                               b, robots['blue'].x_pos, robots['blue'].y_pos,
                                               y, robots['yellow'].x_pos,robots['yellow'].y_pos,
                                               r, robots['red'].x_pos, robots['red'].y_pos)
        return id

    
    
    
