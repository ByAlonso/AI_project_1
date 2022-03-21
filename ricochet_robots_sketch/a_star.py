import copy
from tree import Node
from state import State


class AStar():
    def __init__(self,grid):
        self.grid = copy.deepcopy(grid.grid)
        self.actions = ['up','left','down','right']
        self.robot_clr = ['green','blue','yellow','red', 'gray']
    
    def set_goal(self, goal, robots):
        self.goal = goal
        self.heuristics = self.compute_heuristic(goal)
        
        
    def th_search(self, robots, result):
        path = self.search(robots)
        result['a_star'] = (len(path)-1, path)    

    def search(self, robots):
        # Initial State
        init_state = State(copy.deepcopy(robots))
        init_node = Node(init_state, focus = self.goal.clr_name, depth = 0)

        goal_robot = robots[self.goal.clr_name]
        
        # Search
        visited = {}
        queue = [(init_node, init_node.depth + self.heuristics[goal_robot.y_pos][goal_robot.x_pos])]
        while queue:
            min_ind = queue.index(min(queue, key=lambda item: item[1]))
            current_node = queue.pop(min_ind)[0]
            current_children = self.generate_children(current_node)
            for child in current_children:
                if child.state.is_goal:
                    path = self.get_path(child)
                    return path
                if not visited.get(child.id, False):
                    goal_robot = child.state.robots[self.goal.clr_name]
                    queue.append((child, child.depth + self.heuristics[goal_robot.y_pos][goal_robot.x_pos]))
                    visited[child.id] = True
                            
    def generate_children(self,node):
        children = []
        for action in self.actions:
            for colour in self.robot_clr:
                child = self.generate_child(action,colour,node.state)
                if child is not None:
                    children.append(Node(child,node, focus = self.goal.clr_name, depth = node.depth+1))
        return children
    
    def generate_child(self,dir,robot,state):
        if state.robots[robot].can_move(self.grid,dir,state.robots,state.robots[robot].x_pos,state.robots[robot].y_pos):
            state_copy = copy.deepcopy(state)
            state_copy.set_actions(robot,dir)
            state_copy.robots[robot].move_robot_instant(self.grid,dir,state_copy.robots)
            state_copy.check_if_goal(self.goal)
            return state_copy
        return None
    
    def get_path(self, current_node):
        actions = []
        actions.append(current_node.state.action)
        while current_node.parent != None:
            current_node = current_node.parent
            actions.append(current_node.state.action)
        return actions


    # Pre-compute heuristic for every tile given goal
    def compute_heuristic(self, goal, grid_size=16):
        goal_x = goal.x_pos
        goal_y = goal.y_pos
        
        empty_grid = [[-1 for x in range(grid_size)] for y in range(grid_size)]
        empty_grid[goal_y][goal_x] = 0
        
        # Middle Part
        empty_grid[7][7] = 99999
        empty_grid[7][8] = 99999
        empty_grid[8][7] = 99999
        empty_grid[8][8] = 99999

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
