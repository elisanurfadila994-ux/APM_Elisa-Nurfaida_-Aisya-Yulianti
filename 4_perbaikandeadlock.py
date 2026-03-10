# perbaikan deadlock
import threading
import time
lock1 = threading.Lock()
lock2 = threading.Lock()
def thread1():
    with lock1:
        with lock2:
            print("Thread 1 selesai")
def thread2():
    with lock2:
        with lock1:
            print("Thread 2 selesai")
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)
t1.start()
t2.start()
t1.join()
t2.join()



# Nama : Elisa Nurfaida | Aisya Yulianti 



