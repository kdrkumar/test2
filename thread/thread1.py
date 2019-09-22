import time
import sys

# print(sys.executable)

start = time.perf_counter()


def doSomething():
    print("sleeping for 1 sec")
    time.sleep(1)
    print("Done sleeping")


doSomething()
doSomething()   # async double the time

elapsed = time.perf_counter() - start

print(f'Elapsed time: {elapsed} sec(s)')
