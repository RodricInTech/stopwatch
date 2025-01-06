import time
import threading

class Stopwatch:
    def __init__(self):
        self.running = False
        self.start_time = None
        self.elapsed_time = 0

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self._run()

    def _run(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            print(f"Elapsed Time: {self.elapsed_time:.2f} seconds", end='\r')
            threading.Timer(0.1, self._run).start()

    def stop(self):
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.start_time

    def reset(self):
        self.running = False
        self.start_time = None
        self.elapsed_time = 0

def display_time():
    while True:
        print(f"Current Time: {time.strftime('%H:%M:%S')}", end='\r')
        time.sleep(1)

if __name__ == "__main__":
    stopwatch = Stopwatch()
    threading.Thread(target=display_time, daemon=True).start()

    while True:
        command = input("Enter command (Start /Stop /Reset /Exit): \n").strip().lower()
        if command == "start":
            stopwatch.start()
        elif command == "stop":
            stopwatch.stop()
        elif command == "reset":
            stopwatch.reset()
        elif command == "exit":
            break
        else:
            print("Invalid command")