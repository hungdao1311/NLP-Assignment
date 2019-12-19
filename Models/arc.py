class Arc:
    def __init__(self, type, parent, child):
        self.type = type
        self.parent = parent
        self.child = child
    def __str__(self):
        return self.type + '(' + '(' + ','.join(self.parent) + ')' + ',' + '(' + ','.join(self.child) + ')' + ')'