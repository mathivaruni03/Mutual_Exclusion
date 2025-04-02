import threading
import time
import random
from queue import PriorityQueue

class Process:
    def __init__(self, process_id, total_processes):
        self.process_id = process_id
        self.total_processes = total_processes
        self.timestamp = 0
        self.queue = PriorityQueue()
        self.lock = threading.Lock()
        self.replies = 0

    def request_cs(self):
        with self.lock:
            self.timestamp += 1
            self.queue.put((self.timestamp, self.process_id))
            print(f"Process {self.process_id} requesting CS at time {self.timestamp}")
        
    def receive_request(self, timestamp, sender_id):
        with self.lock:
            self.queue.put((timestamp, sender_id))
            print(f"Process {self.process_id} received request from {sender_id} at time {timestamp}")

    def receive_reply(self):
        with self.lock:
            self.replies += 1
            print(f"Process {self.process_id} received reply ({self.replies}/{self.total_processes - 1})")

    def enter_cs(self):
        while True:
            with self.lock:
                if self.replies == self.total_processes - 1 and self.queue.queue[0][1] == self.process_id:
                    print(f"Process {self.process_id} entering CS")
                    time.sleep(random.uniform(1, 3))  # Simulating critical section execution
                    print(f"Process {self.process_id} exiting CS")
                    self.exit_cs()
                    return
            time.sleep(0.5)

    def exit_cs(self):
        with self.lock:
            self.queue.get()  # Remove itself from the queue
            self.replies = 0  # Reset replies counter
            print(f"Process {self.process_id} finished execution and released CS")

# Simulating three processes
processes = [Process(i, 3) for i in range(3)]

def process_simulation(proc):
    time.sleep(random.uniform(1, 5))
    proc.request_cs()
    for other_proc in processes:
        if other_proc != proc:
            other_proc.receive_request(proc.timestamp, proc.process_id)
    
    time.sleep(1)
    for other_proc in processes:
        if other_proc != proc:
            proc.receive_reply()
    
    proc.enter_cs()

threads = [threading.Thread(target=process_simulation, args=(proc,)) for proc in processes]

for t in threads:
    t.start()

for t in threads:
    t.join()
