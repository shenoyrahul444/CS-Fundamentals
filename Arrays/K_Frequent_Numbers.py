"""
Problem: Top K Frequent Numbers
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.



"""
from heapq import *


class Solution:
    def topKFrequent(self, nums, k):

        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        arr = []
        for num, count in counter.items():
            heappush(arr, [(-1) * count, num])
        result = []

        for i in range(k):
            result.append(heappop(arr)[1])
        return result

nums = [1,1,1,2,2,3]
k = 2
sol =Solution()
print(sol.topKFrequent(nums,k))