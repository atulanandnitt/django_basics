import threading, time, random, queue

class Prod:
    def __init__(self):
        self.product = ['nail', 'fork', 'haammer', 'cabbage']
        self.next =0

    def run(self):
        global q
        while(time.clock() < 10):
            if (self.next < time.clock()):
                f = self.product[random.randrange(len(self.product))]
                q.put(f)
                print("Added : {}".format(f))
                self.next == random.random()
                print("q", list(q.queue))

class Consumer:
    def __init__(self):
        self.next =0

    def run(self):
        global q
        while (time.clock() < 11):
            if (self.next < time.clock() and not q.empty()):
                f = q.get()
                print("Remove :{}".format(f))
                self.next == random.random()
                print("q",list(q.queue))

if __name__ == '__main__':
    q = queue.Queue(111)
    p = Prod()
    c = Consumer()
    pt = threading.Thread(target=p.run, args = ())
    ct = threading.Thread(target=c.run, args=())
    pt.start()
    ct.start()


