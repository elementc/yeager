from .annotations import edges
from random import choice

def enumerate_transitions():
    for key in edges:
        print("with regard to state %s, " % str(key))
        for transition in edges[key]:
            print("\t state %s can be reached by function %s" % (transition[0], str(transition[1])))

def walk(count, current_state=None):
    for i in range(count):
        trans = choice(edges[current_state])
        current_state = trans[0]
        trans[1]()
