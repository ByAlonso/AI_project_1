from copy import deepcopy
from tree import Node
    
class DFS():
    def __init__(self, grid, max_n):
        self.board = deepcopy(grid.grid)
        self.max_n = max_n
                
        # Possible actions and robots
        self.actions = ['up','left','down','right']
        self.robot_clr = ['green', 'blue','yellow','red', 'gray']
        
        self.visited = {}
                        

    def set_goal(self, goal, robots):
        self.goal_clr = goal.clr_name
        self.goal_x = goal.x_pos
        self.goal_y = goal.y_pos
        
        self.visited = {}
        
        # Optimize robot order
        i = self.robot_clr.index(self.goal_clr)
        self.robot_clr.pop(i)
        dists = {self.robot_clr[0]:((robots[self.robot_clr[0]].x_pos - self.goal_x)**2 + (robots[self.robot_clr[0]].y_pos - self.goal_y)**2),
                 self.robot_clr[1]:((robots[self.robot_clr[1]].x_pos - self.goal_x)**2 + (robots[self.robot_clr[1]].y_pos - self.goal_y)**2),
                 self.robot_clr[2]:((robots[self.robot_clr[2]].x_pos - self.goal_x)**2 + (robots[self.robot_clr[2]].y_pos - self.goal_y)**2),
                 self.robot_clr[3]:((robots[self.robot_clr[3]].x_pos - self.goal_x)**2 + (robots[self.robot_clr[3]].y_pos - self.goal_y)**2),
                 }
        self.robot_clr = [k for k, v in sorted(dists.items(), key=lambda item: item[1])]
        self.robot_clr.insert(0, self.goal_clr)
    
    def th_search(self, robots, result):
        path = self.search(robots)
        result['dfs'] = (len(path)-1, path)
        
                                
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
        vis_aux = self.visited.get(id, (0, False))
        if vis_aux[1] and n > vis_aux[0]:
            return None
        else:
            self.visited[id] = (n, True)


        
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
        id = ''
        for robot_color, robot in robots.items():
            c = robot_color[0] if focus == None or focus == robot_color else 'x'
            id += '{}{:02d}{:02d}'.format(c, robot.x_pos, robot.y_pos)
        return id
    
    
    
