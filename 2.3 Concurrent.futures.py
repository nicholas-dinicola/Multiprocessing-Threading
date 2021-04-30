import time
import concurrent.futures

start = time.perf_counter()

# USING CONCURRENT.FUTURES WITH MORE VALUES IN THE FUNCTION USING LIST COMPREHENSION

# Create th efunction and return the values this time as a string
def do_something(seconds):
    print(f"Sleeping for {seconds} second...")
    time.sleep(seconds)
    return f"Done sleeping!... {seconds}"


# Use concurrent futures pool
with concurrent.futures.ProcessPoolExecutor() as executor:  # concurrent.futures.ThreadPoolExecutor() for Threading
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

# Using map we do not need the for loop anymore
#   for result in results:
#       print(result)

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds")