import time
import threading

def background_task():
    while True:
        print("Background task is running...")
        time.sleep(10)