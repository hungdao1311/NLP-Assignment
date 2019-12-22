from .data_type import *
from .utils import *
class Transition(object):

    # Define set of transitions
    LEFT_ARC = 'LEFTARC'
    RIGHT_ARC = 'RIGHTARC'
    SHIFT = 'SHIFT'
    REDUCE = 'REDUCE'

    def __init__(self):
        raise ValueError('Do not construct this object!')

    @staticmethod
    def left_arc(parser, type, wi, wj):
        parser.stack.pop()
        if wi.child:
            wi.child.append(wj)
        else:
            wi.child = [wj]
        if wj.parent:
            wj.parent.append(wi)
        else:
            wj.parent = [wi]
        parser.arcs.append(Arc(type, wj, wi))

    @staticmethod
    def right_arc(parser, type, wi, wj):
        parser.buffer.pop(0)
        parser.stack.append(wj)
        if wi.child:
            wi.child.append(wj)
        else:
            wi.child = [wj]
        if wj.parent:
            wj.parent.append(wi)
        else:
            wj.parent = [wi]
        parser.arcs.append(Arc(type, wi, wj))

    @staticmethod
    def reduce(parser):
        parser.stack.pop()

    @staticmethod
    def shift(parser):
        top_buffer = parser.buffer.pop(0)
        parser.stack.append(top_buffer)
    
