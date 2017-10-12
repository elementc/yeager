from collections import defaultdict
from functools import wraps

nodes = set()
edges = defaultdict(list)

def filter_node_id(name):
    if isinstance(name, str):
        return name.lower()
    else:
        return name

def add_node(name):
    nodes.add(filter_node_id(name))

def add_edge(node_from, node_to, traversal_method):
    edges[filter_node_id(node_from)].append((filter_node_id(node_to), traversal_method),)

def state_transition(state_from, state_to):
    def decorator(func):
        if not isinstance(state_from, list):
            states_from = [state_from,]
        else:
            states_from = state_from
        if not isinstance(state_to, list):
            states_to = [state_to,]
        else:
            states_to = state_to
        for s_frm in states_from:
            for s_to in states_to:
                # print("establishing %s as a transition from %s to %s" % (str(func), str(s_frm), str(s_to)),)
                @wraps(func)
                def transition_function(*args, **kwargs):
                    print("executing function %s, current state -> %s" % (str(func), str(s_to)))
                    return func(*args, **kwargs)
                add_node(s_frm)
                add_node(s_to)
                add_edge(s_frm, s_to, transition_function)
        return func
    return decorator
