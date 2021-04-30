import time
import multiprocessing

# RUNNNING A FUNCTION TWO TIMES ASYNCHRONOUSLY ON MULTIPLE CPU CORES


start = time.perf_counter()

# Create a function
def do_something():
    print("Sleeping for 1 second...")
    time.sleep(1)
    print("Done sleeping!")


# Use multiprocessing
p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

# We need to start the process for both
p1.start()
p2.start()

# The process will finish before moving on with the process
p1.join()
p2.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds")