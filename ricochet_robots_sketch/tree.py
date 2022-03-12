class Node():
    def __init__(self, state, parent=None, focus = None):
        self.state = state
        self.parent = parent
        self.id = self.def_id(focus)
        
    # Define ID to easily compare if this state was already visited
    def def_id(self, focus):
        g = 'g' if focus == None or focus == 'green' else 'd'
        b = 'b' if focus == None or focus == 'blue' else 'd'
        y = 'y' if focus == None or focus == 'yellow' else 'd'
        r = 'r' if focus == None or focus == 'red' else 'd'
        id = '{}{:02d}{:02d}{}{:02d}{:02d}{}{:02d}{:02d}{}{:02d}{:02d}'.format(
                                               g, self.state.robots['green'].x_pos, self.state.robots['green'].y_pos,
                                               b, self.state.robots['blue'].x_pos, self.state.robots['blue'].y_pos,
                                               y, self.state.robots['yellow'].x_pos, self.state.robots['yellow'].y_pos,
                                               r, self.state.robots['red'].x_pos, self.state.robots['red'].y_pos)
        return id
        
                        
