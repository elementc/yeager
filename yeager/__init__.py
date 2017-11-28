from .annotations import nodes, edges, edge_weights, set_edge_weight, filter_node_id, state_transition
from random import choice

state_blacklist = set()
trans_blacklist = set()

def add_state_to_blacklist(state):
    state_blacklist.add(filter_node_id(state))

def add_transition_to_blacklist(transition):
    trans_blacklist.add(transition)

def remove_state_from_blacklist(state):
    state_blacklist.remove(filter_node_id(state))

def remove_transition_from_blacklist(transition):
    trans_blacklist.remove(transition)

def calculate_choices(edge_options):
    weighted_choices = []
    for edge in edge_options:
        # obey blacklists
        if edge[0] in state_blacklist or edge[1] in trans_blacklist:
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
            print("\t state %s can be reached by function %s (weight %d)%s" %
                (transition[0], str(transition[1]),
                edge_weights[transition[1]],
                " (BLACKLISTED)" if
                transition[0] in state_blacklist or
                transition[1] in trans_blacklist
                else "")
            )

class ExitStateReachedException(Exception):
    pass

class NoStatesToStepToException(Exception):
    pass

class _YeagerDefaultExitState_: # users must explicitly set the exit state in order to trigger exit state options...
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

__all__=[enumerate_transitions, walk, reachable_states, orphaned_states, NoStatesToStepToException, set_edge_weight, add_state_to_blacklist, add_transition_to_blacklist, remove_state_from_blacklist, remove_transition_from_blacklist, state_transition, nodes, edges]
