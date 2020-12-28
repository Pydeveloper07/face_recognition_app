import BrainOfFront
from WindowLoader import WindowManager

if __name__ == "__main__":
    BrainOfFront.RunMain()
    window_loader = WindowManager()
    window_loader.start()
    print("Is this end")
    BrainOfFront.CloseAll()
