from yeager.annotations import state_transition
from yeager import enumerate_transitions, walk, reachable_states, orphaned_states, add_state_to_blacklist
from collections import defaultdict

@state_transition(None, "login-page")
def launch_app(arg):
    print("launching application...")

@state_transition("login-page", "home-page")
def log_in(arg):
    print("logging in...")

@state_transition("home-page", "settings-page")
def open_settings(arg):
    print("opening the settings page...")

@state_transition("settings-page", "home-page")
def save_settings(arg):
    print("saving settings...")

@state_transition("home-page", "map-editor")
def load_map(arg):
    print("loading a map...")

@state_transition("map-editor", "map-editor", weight=15)
def draw_on_map(arg):
    print("drawing on the map...")

@state_transition("map-editor", "map-editor")
def save_map(arg):
    print("saving the map...")

@state_transition("map-editor","home-page")
def close_map(arg):
    print("closing the map...")

@state_transition("map-editor", "map-editor")
def export_map(arg):
    arg["exports"].append("exported a map")
    print("exporting the map...")

@state_transition("home-page", "map-editor")
def new_map(arg):
    arg["maps"].append("created a new map")
    print("creating new map...")

@state_transition(["map-editor", "home-page", "settings-page"], "login-page")
def log_out(arg):
    print("logging out...")
    # raise Exception("buggy code")

@state_transition("mab-editor", "home-page")
def misspelled_logout(arg):
    print("This will never run because 'mab-editor' is an orphaned state.")

@state_transition("login-page", None)
def quti(arg):
    print("quitting the application")


if __name__ == "__main__":
    # debug function to dump the entire state graph to the console
    add_state_to_blacklist("settings-page")
    # enumerate_transitions()

    # debug function returns a list of all states reachable in the graph (BFS).
    # print("from the default state of None, reachable states:")
    # for state in reachable_states():
    #     print("\t%s" % state)
    #
    # # debug function returns a list of all states NOT reachable in the graph (reachable_states -> set subtraction)
    # print("from the default state of None, unreachable states:")
    # for state in orphaned_states():
    #     print("\t%s" % state)
    #
    # # reachable_states, orphaned_states, and walk take an optional arg (default None) to define "starting state"
    # # overridable like this:
    # print("from the custom state of mab-editor, reachable states:")
    # for state in reachable_states("mab-editor"):
    #     print("\t%s" % state)

    # utility function to walk on the graph:
    dic = defaultdict(list)
    walk(25, arg=dic)
