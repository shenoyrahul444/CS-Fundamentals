from heapq import *

arr = [[6,2],[1,4],[7,5],[3,8],[0,9]]

l = []
for n in arr:
    heappush(l,[n[1],n[0]])
i = 0
while l:
    print(heappop(l))

