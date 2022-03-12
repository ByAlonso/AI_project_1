from tree import Node
from state import State
import time
import copy
import sys

class BFS():
    def __init__(self,grid):
        self.grid = copy.deepcopy(grid.grid)
        self.actions = ['up','left','down','right']
        self.robot_clr = ['green','blue','yellow','red']
        
                                
    def set_goal(self, goal, robots):
        self.goal = goal

    def search(self, robots):
        # Initial State
        init_state = State(copy.deepcopy(robots))
        init_node = Node(init_state, focus = self.goal.clr_name)

        # Search
        visited = [init_node]
        queue = [init_node]
        while queue:
            current_node = queue.pop(0)
            current_children = self.generate_children(current_node)
            for child in current_children:
                if child.state.is_goal:
                    path = self.get_path(child)
                    return path
                if not self.node_is_visited(visited, child):
                    visited.append(child)
                    queue.append(child)
                
                            
    def generate_children(self,node):
        children = []
        for action in self.actions:
            for colour in self.robot_clr:
                child = self.generate_child(action,colour,node.state)
                if child is not None:
                    children.append(Node(child,node, focus = self.goal.clr_name))
        return children
    
    def generate_child(self,dir,robot,state):
        if state.robots[robot].can_move(self.grid,dir,state.robots):
            state_copy = copy.deepcopy(state)
            state_copy.set_actions(robot,dir)
            while state_copy.robots[robot].move_robot(self.grid,dir,state_copy.robots):
                pass
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
    
    def node_is_visited(self, visited, node):
        for v in visited:
            if node.id == v.id:
                return True
        return False
