import time
import concurrent.futures

start = time.perf_counter()

# USING CONCURRENT.FUTURES

# Create th efunction and return the values this time as a string
def do_something(seconds):
    print(f"Sleeping for {seconds} second...")
    time.sleep(seconds)
    return f"Done sleeping!... {seconds}"


# Use concurrent futures pool
with concurrent.futures.ProcessPoolExecutor() as executor:  # concurrent.futures.ThreadPoolExecutor() for Threading

    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 1)

    print(f1.result())
    print(f2.result())

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds")