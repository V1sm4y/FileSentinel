import os
from core.monitor import start_watchdog

if __name__ == "__main__":
    
    FOLDER_TO_WATCH = "./test_directory"
    
    if not os.path.exists(FOLDER_TO_WATCH):
        os.makedirs(FOLDER_TO_WATCH)
        print(f"[*] Created test directory: {FOLDER_TO_WATCH}")
        
    start_watchdog(FOLDER_TO_WATCH)