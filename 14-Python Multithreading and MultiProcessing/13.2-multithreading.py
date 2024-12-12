## Multithreading
## When to use Multi Threading
### I/O - bound tasks:Tasks that spends more time waiting for I/O operations
# (eg:- file operations,network requests)
#  Concurrent execution: When you want to improve the throughput of your application by performing multiple operation concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter:{letter}")
# #Single threading
# t=time.time()
# print_numbers()
# print_letter()
# finished_time=time.time()-t
# print(finished_time)

##Multi-threading
## Create 2 threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)

t=time.time()
##Start the thread
t1.start()
t2.start()

### wait for the  threads to complete
finished_time=time.time()-t
print(finished_time)