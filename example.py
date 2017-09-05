from yeager.annotations import state_transition
from yeager import enumerate_transitions, walk

@state_transition(None, "login-page")
def launch_app():
    print("launching application...")

@state_transition("login-page", "home-page")
def log_in():
    print("logging in...")

@state_transition("home-page", "settings-page")
def open_settings():
    print("opening the settings page...")

@state_transition("settings-page", "home-page")
def save_settings():
    print("saving settings...")

@state_transition("home-page", "map-editor")
def load_map():
    print("loading a map...")

@state_transition("map-editor", "map-editor")
def draw_on_map():
    print("drawing on the map...")

@state_transition("map-editor", "map-editor")
def save_map():
    print("saving the map...")

@state_transition("map-editor","home-page")
def close_map():
    print("closing the map...")

@state_transition("map-editor", "map-editor")
def export_map():
    print("exporting the map...")

@state_transition("home-page", "map-editor")
def new_map():
    print("creating new map...")

@state_transition(["map-editor", "home-page", "settings-page"], "login-page")
def log_out():
    print("logging out...")


if __name__ == "__main__":
    enumerate_transitions()
    walk(100)
