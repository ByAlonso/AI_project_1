from tree import Node
from state import State
import time
import copy
import sys
class BFS():
    def __init__(self,grid):
        self.grid = grid.grid
        self.actions = ['up','left','down','right']
        self.robot_clr = ['green','blue','yellow','red']
        self.init_state = State(grid)
        self.init_node = Node(self.init_state,None)
        self.init_state.print_state()
            
    def generate_tree(self):
        children_aux = []
        selected_node = self.init_node
        self.generate_children(selected_node)
        current_children = selected_node.children
        if any([s.state.is_goal for s in current_children]):
            return [s for s in current_children if s.state.is_goal][0]
        n = 1
        while not any([s.state.is_goal for s in current_children]):
            print(n,len(current_children))
            for child in current_children:
                self.generate_children(child)
                if any([s.state.is_goal for s in child.children]):
                    return [s for s in child.children if s.state.is_goal][0]
                children_aux.extend(child.children)
            current_children = children_aux
            children_aux = []
            n+=1
            
    def generate_children(self,node):
        for action in self.actions:
            for colour in self.robot_clr:
                child = self.generate_child(action,colour,node.state)
                if child is not None:
                    node.children.append(Node(child,node))
    
    def generate_child(self,dir,robot,state):
        state_copy = copy.deepcopy(state)
        if state_copy.robots[robot].can_move(state_copy.grid,dir,state_copy.robots):
            state_copy.set_actions(robot,dir)
            state_copy.grid_.select_robot(state_copy.robots[robot].x_pos,state_copy.robots[robot].y_pos)
            while state_copy.robots[robot].move_robot(state_copy.grid,dir,state_copy.robots):
                pass
            state_copy.check_if_goal()
            return state_copy
        return None
