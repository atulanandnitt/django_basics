import multiprocessing
from multiprocessing import Process, current_process
import os
def child1():
        print(current_process().name)
        print("I am child1")
def child2():
        print(current_process().name)
        print("I am child2")

if __name__=="__main__":
   # print("Parent ID",os.getpid())
   p1=Process(target=child1)
   # p2=Process(target=child2,name='Child 2')
   p1.start()
   # p2.start()
   # p1.join()
   # p2.join()
   print("We're done")