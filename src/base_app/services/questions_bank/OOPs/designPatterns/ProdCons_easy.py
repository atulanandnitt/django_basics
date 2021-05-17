import threading, time, random, queue

class Prod:
    def __init__(self):
        self.product = ['nail', 'fork', 'haammer', 'cabbage']
        self.next =0

    def run(self):
        global q
        while 1:
            if (not q.full()):
                f = self.product[random.randrange(len(self.product))]
                q.put(f)
                print("Added : {}".format(f))
                print("q", list(q.queue))

class Consumer:
    def __init__(self):
        self.next =0

    def run(self):
        global q
        while 1:
            if (not q.empty()):
                f = self.product[random.randrange(len(self.product))]
                f = q.get()
                print("Remove :{}".format(f))
                print("q",list(q.queue))

if __name__ == '__main__':
    maxsize = 11
    q = queue.Queue(maxsize)
    p = Prod()
    c = Consumer()
    pt = threading.Thread(target=p.run, args = ())
    ct = threading.Thread(target=c.run, args=())
    pt.start()
    ct.start()


