class Node():
    def __init__(self, state, parent=None, focus = None, depth = 0):
        self.state = state
        self.parent = parent
        self.id = self.def_id(focus)
        self.depth = depth
        
    # Define ID to easily compare if this state was already visited
    def def_id(self, focus):
        id = ''
        for robot_color, robot in self.state.robots.items():
            c = robot_color[0] if focus == None or focus == robot_color else 'x'
            id += '{}{:02d}{:02d}'.format(c, robot.x_pos, robot.y_pos)
        return id
        
                        
