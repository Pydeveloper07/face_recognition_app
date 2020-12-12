from WindowLoader import WindowManager
import BrainOfFront

if __name__ == "__main__":
    BrainOfFront.RunMain()
    window_loader = WindowManager()
    window_loader.load_login_window()
    BrainOfFront.CloseAll()
