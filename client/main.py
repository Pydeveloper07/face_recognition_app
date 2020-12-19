from WindowLoader import WindowManager
import BrainOfFront
import sys
import util_funcs

if __name__ == "__main__":
    BrainOfFront.RunMain()
    window_loader = WindowManager()
    window_loader.start()
    BrainOfFront.CloseAll()
