from .annotations import edges
from random import choice

def enumerate_transitions():
    for key in edges:
        print("with regard to state %s, " % str(key))
        for transition in edges[key]:
            print("\t state %s can be reached by function %s" % (transition[0], str(transition[1])))

class ExitStateReachedException(Exception):
    pass

class NoStatesToStepToException(Exception):
    pass

class _YeagerDefaultExitState_: # users must explicitly set the exit state to None in order to trigger exit state options...
    pass

def walk(count=None, exit_state=_YeagerDefaultExitState_, start_state=None, **kwargs):
    current_state = start_state
    def step():
        nonlocal current_state
        if len(edges[current_state]) == 0:
            raise NoStatesToStepToException("There are no states that yeager knows how to transition to from state %s." % current_state)
        trans = choice(edges[current_state])
        current_state = trans[0]
        trans[1](**kwargs)
        if current_state is exit_state:
            raise ExitStateReachedException(current_state)

    if count:
        for i in range(count):
            step()
    else: # must be infinite walk or walk until exit state
        try:
            while True:
                step()
        except ExitStateReachedException as e:
            print("Reached anticipated exit state (%s) normally." % str(e))
        except KeyboardInterrupt:
            print("Interrupted by keyboard, quitting.")

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

__all__=[enumerate_transitions, walk, reachable_states, orphaned_states, NoStatesToStepToException]
