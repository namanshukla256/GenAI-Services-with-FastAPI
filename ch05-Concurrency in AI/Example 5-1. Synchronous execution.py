import time

def task():
    print("Start of sync task")
    time.sleep(5) # Simulate a blocking I/O operation
    print("After 5 seconds of sleep")

start = time.time()

for _ in range(3):
    task()

duration = time.time() - start
print(f"\n Process completed in P{duration} seconds")