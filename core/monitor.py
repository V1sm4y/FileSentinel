import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from core.hasher import calculate_file_hash

class FIMEventHandler(FileSystemEventHandler):
    
    
    def on_created(self, event):
        if not event.is_directory:
            file_hash = calculate_file_hash(event.src_path)
            print(f"[+] CREATED: {event.src_path} | Hash: {file_hash}")

    def on_modified(self, event):
        if not event.is_directory:
            file_hash = calculate_file_hash(event.src_path)
            print(f"[*] MODIFIED: {event.src_path} | New Hash: {file_hash}")

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"[-] DELETED: {event.src_path}")

def start_watchdog(target_directory):
    print(f"[*] Starting FileSentinel observer on: {target_directory}...")
    
    event_handler = FIMEventHandler()
    observer = Observer()
    observer.schedule(event_handler, target_directory, recursive=True)
    observer.start()
    
    print("[*] Monitoring active. Press Ctrl+C to stop.\n")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[*] Stopping observer...")
        observer.stop()
        
    observer.join()