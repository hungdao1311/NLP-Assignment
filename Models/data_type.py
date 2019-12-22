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

class Predicate:
    def __init__(self, pred, operand):
        self.pred = pred
        self.operand = operand
    def __str__(self):
        return self.pred + '(' + self.operand + ')'

class ATime:
    def __init__(self, bus = None, dest = None, time = None):
        self.bus = bus
        self.dest = dest
        self.time = time

    def __str__(self):
        return "(ATIME " + (self.bus if self.bus else "?b") + " " + self.dest + " " + (self.time if self.time else "?t") + ")"
    
    def __eq__(self, other):
        if self.bus is not None:
            if self.bus != other.bus:
                return False
        if self.dest is not None:
            if self.dest != other.dest:
                return False
        if self.time is not None:
            if self.time != other.time:
                return False
        return True

class DTime:
    def __init__(self, bus = None, dep = None, time = None):
        self.bus = bus
        self.dep = dep
        self.time = time
    def __str__(self):
        return "(DTIME " + self.bus if self.bus else "?b" + " " + self.dest + " " + (self.time if self.time else "?t") + ")"
    def __eq__(self, other):
        if self.bus:
            if self.bus != other.bus:
                return False
        if self.dest:
            if self.dest != other.dest:
                return False
        if self.time:
            if self.time != other.time:
                return False
        return True

class RunTime: 
    def __init__(self, bus = None, dep = None, dest = None, time = None):
        self.bus = bus
        self.dep = dep
        self.dest = dest
        self.time = time
    def __str__(self):
        return "(RUN-TIME " + self.bus + " " + self.dep + " " + self.dest + " " + (self.time if self.time else "?t") + ")"
    def __eq__(self, other):
        if self.bus:
            if self.bus != other.bus:
                return False
        if self.dep:
            if self.dep != other.dep:
                return False
        if self.dest:
            if self.dest != other.dest:
                return False
        if self.time:
            if self.time != other.time:
                return False
        return True
