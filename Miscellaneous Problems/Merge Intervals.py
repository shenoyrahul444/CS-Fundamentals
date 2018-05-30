# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == [] or len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: x.start)
        merged = [intervals[0]]
        for interval in intervals[1:]:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            ref = merged.pop()
            if ref.end < interval.start:
                merged.append(ref)
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                ref.end = max(ref.end, interval.end)
                merged.append(ref)
        return merged

def printNodes(nodes):
    for node in nodes:
        print("{%d : %d)" % (node.start,node.end))

sol = Solution()
a = [[1,3],[8,10],[15,18],[2,6]]
arr=[]
for s,e in a:
    arr.append(Interval(s,e))
printNodes(arr)
print("\nAfter Merging:\n")

merged = sol.merge(arr)
printNodes(merged)