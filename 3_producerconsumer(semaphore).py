import threading
import time
from threading import Semaphore

buffer = [3]
empty = Semaphore(5)
full = Semaphore(0)

def producer():
 for i in range(10):
     empty.acquire()
     buffer.append(i)
     print("Produksi:", i)
     full.release()
     time.sleep(0.1)

def consumer():
 for i in range(10):
    full.acquire()
    item = buffer.pop(0)
    print("Konsumsi:", item)
    empty.release()

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()


#Nama: Aisya Yulianti | Elisa Nurfaida