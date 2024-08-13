import queue

n = int(input())

q = queue.Queue()
for i in range(n):
    q.put(i + 1)

for i in range(n - 1):
    q.get()
    q.put(q.get())

print(q.get())