import sys

import gui
import cli

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # GUI
        print("Starting SceneFromGIS GUI")
        gui.start(sys.argv)
    else:
        # CLI
        print("Starting SceneFromGIS CLI")
        cli.start(sys.argv)
