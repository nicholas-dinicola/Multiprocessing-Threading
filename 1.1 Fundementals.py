import time
import multiprocessing


# RUNNING A FUNCTION TWO TIMES WITHOUT MULTIPROCESSING

start = time.perf_counter()

# Create a function


def do_something():
    print("Sleeping for 1 second...")
    time.sleep(1)
    print("Done sleeping!")


# Instead of doing like that we can use multiprocessing to do both at the same time
do_something()
do_something()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds")