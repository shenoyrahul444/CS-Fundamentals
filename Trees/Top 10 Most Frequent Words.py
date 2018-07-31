from heapq import *
def countMax10(s):
    s = s.lower()
    counter = {}
    word = ""
    for char in s:
        if char.isalpha():
            word += char
        else:
            if word != "":
                if word in counter:
                    counter[word] += 1
                else:
                    counter[word] = 1
            word = ""
    heap = []
    i = 0
    for word,count in counter.items():
        if i == 3:
            if count > heap[0][0] :
                heappop(heap)
                heappush(heap,(count,word))
        else:
            i+=1
            heappush(heap,(count,word))

    return  heap

s = "My Name is Rahul and I bombed the Amazon  amazon interview bad. amazon is a good company and I would love the atmosphere."
print(countMax10(s))