class TreeNode:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
        self.children = []
    
    def add_child(self, node):
        self.children.append(node)

    def return_coords(self): 
        result = []
        to_print = [self]
        while to_print:
            current = to_print.pop(0)
            result.append((current.x, current.y))
            to_print.extend(current.children)

        return result