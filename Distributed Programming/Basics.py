class C(object):
    def __init__(self, i, n):
        self.i = i
        self.n = n

    def show(self):
        # print('%s: %.2f' % (self.i, self.n))
        print(str(self.i) + " " + str(self.n))

def compute(obj):
    # obj is an instance of C
    import time
    time.sleep(obj.n)

    obj.show()  # the output is stored in job.stdout
    return obj.n

if __name__ == '__main__':
    import random, dispy
    # 'compute' needs definition of class C, so include in 'depends'
    cluster = dispy.JobCluster(compute, depends=[C])
    jobs = []
    for i in range(10):
        c = C(i, random.uniform(1, 3)) # create object of C
        job = cluster.submit(c) # it is sent to a node for executing 'compute'
        job.id = c # store this object for later use
        jobs.append(job)
    for job in jobs:
        job() # wait for job to finish
        # print('%s: %.2f / %s' % (job.id.i, job.result, job.stdout))
        print("JOB ID i: ",job.id.i,job.result,job.stdout)