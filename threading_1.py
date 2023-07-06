import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

def main():
    # Normal code
    # func(4)
    # func(2)
    # func(1) 

    time1 = time.perf_counter()
    # same code using threading     
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    time2 = time.perf_counter()
    print(time2-time1)

def poolingDemo():
    time1 = time.perf_counter()    
    with ThreadPoolExecutor() as executor: #max_workers=4
        # future1 = executor.submit(func, 1)
        # future2 = executor.submit(func, 4)
        # future3 = executor.submit(func, 2)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())

        l = [1,4,2]
        results = executor.map(func, l)

        # for result in results:
        #     print(result)

    time2 = time.perf_counter()     
    print(time2 - time1)   
# main()
poolingDemo()