import time
import threading

# import sys
# print(sys.executable)

start = time.perf_counter()


def doSomething():
    print("sleeping for 1 sec")
    time.sleep(1)
    print("Done sleeping")


t1 = threading.Thread(target=doSomething)
t2 = threading.Thread(target=doSomething)

t1.start()
t2.start()

elapsed = time.perf_counter() - start

print(f'Elapsed time: {elapsed} sec(s)')
