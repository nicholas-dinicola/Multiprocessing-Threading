import time
import multiprocessing

# RUNNING A FUNCTION MULTIPLE TIMES WITH MULTIPLE VALUES AS AN ARGUMENT ON MULTIPLE CORE

start = time.perf_counter()

# Use multi processing passing a list of values in the arguments in the function


def do_something(seconds):
    print(f"Sleeping for {seconds} second...")
    time.sleep(seconds)
    print("Done sleeping!")


# List to store all the processes to join after have joined them
processes = []

for _ in range(10):
    p = multiprocessing.Process(target=do_something, args=[1.5])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds")
