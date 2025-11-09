import sys
import time
import threading
import os

stop_event = threading.Event()
loading_thread = None

def hide_cursor():
    if os.name == 'nt':  
        os.system('echo off')
    else:  
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

def show_cursor():
    if os.name == 'nt':
        os.system('echo on')
    else:  
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

def loading():
    spinner_chars = ['    ', '.   ', '..  ', '... ', '....']
    i = 0
    message = "Fetching information"
    
    
    hide_cursor()
    
    try:
        while not stop_event.is_set():
            sys.stdout.write(f"\r{message} {spinner_chars[i]}")
            sys.stdout.flush()
            time.sleep(0.3)
            i = (i + 1) % len(spinner_chars)
        
        sys.stdout.write('\r' + ' ' * (len(message) + 5) + '\r')
        sys.stdout.flush()

    finally: 
        show_cursor()

def start_loading():
    global loading_thread
    if loading_thread is None or not loading_thread.is_alive():  
        stop_event.clear()
        loading_thread = threading.Thread(target=loading)
        loading_thread.daemon = True
        loading_thread.start()

def stop_loading():
    global loading_thread
    if loading_thread and loading_thread.is_alive():
        stop_event.set()  
        loading_thread.join()
        loading_thread = None
    show_cursor()
