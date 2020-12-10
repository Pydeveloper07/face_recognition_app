from WindowLoader import WindowManager
import BrainOfFront

if __name__ == "__main__":
    BrainOfFront.RunMain()
    window_loader = WindowManager()
    window_loader.load_dashboard_window()
    BrainOfFront.CloseAll()
