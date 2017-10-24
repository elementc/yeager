from .annotations import edges, edge_weights, set_edge_weight, filter_node_id
from random import choice

state_blacklist = set()

def add_state_to_blacklist(state):
    state_blacklist.add(filter_node_id(state))

def calculate_choices(edge_options):
    weighted_choices = []
    for edge in edge_options:
        # obey blacklist
        if edge[0] in state_blacklist:
            continue
        else:
            # obey weights
            for i in range(edge_weights[edge[1]]):
                weighted_choices.append(edge)
    return weighted_choices

def enumerate_transitions():
    for key in edges:
        print("with regard to state %s, " % str(key))
        for transition in edges[key]:
            print("\t state %s can be reached by function %s (weight %d)%s" % (transition[0], str(transition[1]), edge_weights[transition[1]], " (BLACKLISTED)" if transition[0] in state_blacklist else "") )

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
        weighted_choices = calculate_choices(edges[current_state])
        if len(weighted_choices) == 0:
            raise NoStatesToStepToException("There are no states that yeager knows how to transition to from state %s." % current_state)
        trans = choice(weighted_choices)
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

__all__=[enumerate_transitions, walk, reachable_states, orphaned_states, NoStatesToStepToException, set_edge_weight]
