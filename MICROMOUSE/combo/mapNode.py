
class mapNode:
    def __init__(self):
        self.types = 8
        #0 = no wall
        #1 = wall

        #options only matter if type=0
        self.options = 0
        #0 = no mouse has been there
        #1 = a mouse has been there
        #2 = a mouse has been there, no more paths

    def __getTypes__(self):
        return self.types

    def __setTypes__(self):
        self.types = value

    def __getOptions__(self):
        return self.options

    def __setOptions__(self):
        self.options = options
