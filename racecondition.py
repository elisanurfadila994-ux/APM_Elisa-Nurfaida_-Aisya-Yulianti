
# Online Python - IDE, Editor, Compiler, Interpreter
import threading
import time
counter = 0
def increment():
  global counter
  for _ in range(100000):
    temp = counter
    time.sleep(0)
    counter = temp + 1
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)
t1.start()
t2.start()
t1.join()
t2.join()
print("Nilai counter:", counter)


# Nama : Elisa NUrfaida | Aisya Yulianti