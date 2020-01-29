import queue
import threading
num_workers = 4
q = queue.Queue()#FIFO - First in First Out
#q = queue.LifoQueue()#last in first out
#q = queue.PriorityQueue()#priorität angeben

def do_work(item):
    print(item)

def worker():
    while True:
        item = q.get()
        if item is None:
            break
        do_work(item)
        q.task_done()

threads = []
for i in range(num_workers):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for i in range(100):
    q.put(i)


for t in threads:
    t.join()