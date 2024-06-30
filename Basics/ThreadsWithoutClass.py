import time
import threading


def check(end):
    for i in range(1,end):
        print('start',i, threading.current_thread(), threading.current_thread().is_alive())
        time.sleep(1)
        print('stop',i)
        print(threading.current_thread().is_alive())

x = threading.Thread(target=check,args=(2,),name="SQLRead",daemon=True)
x.start()
time.sleep(1)
x1 = threading.Thread(target=check,args=(3,),name="EXCEL")
x1.start()
x.join()
x1.join()
print('Thread status',x1.is_alive())