import multiprocessing

res = []

def getCube(arr):
    global res
    for i in range(len(arr) - 1):
        for j in range(i,len(arr)):
            res.append(arr[i]*arr[j])
    print(res)
    print("*** Process ends inside function*** ")

if __name__ == "__main__":
    import os
    a = [1,2,4,5,6,2,4,3]
    p1 = multiprocessing.Process(target=getCube,args=(a,))
    print("** P1 started **")
    p1.start()
    
    print("PID of the Main", os.getpid())
    print("P1 id: ",p1.pid)
    print("Is Alive",p1.is_alive())
    # print(res)
    p1.join()
    print(res)
    print("*** Process ends in main *** ")
    print("Is Alive", p1.is_alive())