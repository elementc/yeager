from .annotations import edges
from random import choice

def enumerate_transitions():
    for key in edges:
        print("with regard to state %s, " % str(key))
        for transition in edges[key]:
            print("\t state %s can be reached by function %s" % (transition[0], str(transition[1])))

def walk(count, current_state=None, **kwargs):
    for i in range(count):
        trans = choice(edges[current_state])
        current_state = trans[0]
        trans[1](**kwargs)

def reachable_states(start=None):
    can_reach = set([start])
    queue = [start]
    current=None
    while (len(queue) > 0):
        current = queue.pop()
        for item in edges[current]:
            candidate = item[0]
            if candidate not in can_reach:
                can_reach.add(candidate)
                queue.insert(0, candidate)
    return can_reach

def orphaned_states(start=None):
    can_reach = reachable_states(start)
    orphaned_states = []
    for state in edges.keys():
        if state not in can_reach:
            orphaned_states.append(state)
    return orphaned_states
