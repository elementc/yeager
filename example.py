from yeager.annotations import state_transition
from yeager import enumerate_transitions, walk, reachable_states, orphaned_states
from selenium import webdriver

@state_transition(None, "login-page")
def launch_app(test=None):
    print("launching application...")
    test.get("https://chrome.google.com")

@state_transition("login-page", "home-page")
def log_in(test=None):
    print("logging in...")
    test.get("https://www.mozilla.org/en-US/firefox/")

@state_transition("home-page", "settings-page")
def open_settings(test=None):
    print("opening the settings page...")

@state_transition("settings-page", "home-page")
def save_settings(test=None):
    print("saving settings...")

@state_transition("home-page", "map-editor")
def load_map(test=None):
    print("loading a map...")

@state_transition("map-editor", "map-editor")
def draw_on_map(test=None):
    print("drawing on the map...")

@state_transition("map-editor", "map-editor")
def save_map(test=None):
    print("saving the map...")

@state_transition("map-editor","home-page")
def close_map(test=None):
    print("closing the map...")

@state_transition("map-editor", "map-editor")
def export_map(test=None):
    print("exporting the map...")

@state_transition("home-page", "map-editor")
def new_map(test=None):
    print("creating new map...")

@state_transition(["map-editor", "home-page", "settings-page"], "login-page")
def log_out(test=None):
    test.get("https://chrome.google.com")
    print("logging out...")

@state_transition("mab-editor", "home-page")
def misspelled_logout(test=None):
    print("This will never run because 'mab-editor' is an orphaned state.")


if __name__ == "__main__":
    # debug function to dump the entire state graph to the console
    enumerate_transitions()

    # debug function returns a list of all states reachable in the graph (BFS).
    print("from the default state of None, reachable states:")
    for state in reachable_states():
        print("\t%s" % state)

    # debug function returns a list of all states NOT reachable in the graph (reachable_states -> set subtraction)
    print("from the default state of None, unreachable states:")
    for state in orphaned_states():
        print("\t%s" % state)

    # reachable_states, orphaned_states, and walk take an optional arg (default None) to define "starting state"
    # overridable like this:
    print("from the custom state of mab-editor, reachable states:")
    for state in reachable_states("mab-editor"):
        print("\t%s" % state)

    # utility function to walk on the graph:
    walk(10, test=webdriver.Chrome())
