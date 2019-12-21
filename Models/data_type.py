class Arc:
    def __init__(self, type, source, dest):
        self.type = type
        self.source = source
        self.dest = dest
    def __str__(self):
        return self.type + '(' + self.source.token + ',' + self.dest.token + ')'

class WordNode:
    def __init__(self, token, tag, parent = [], child = []):
        self.token = token
        self.tag = tag
        self.parent = parent
        self.child = child

class Pattern:
    def __init__(self, type, var, animate):
        self.type = type
        self.var = var 
        self.animate = animate
    def __str__(self):
        return self.type + '(' + self.var + ', ' + self.animate + ')'