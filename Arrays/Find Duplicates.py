"""

"""


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicate = None
        n = len(nums)
        currSum = sum(nums)
        # Way 1: To find Duplicate in Constant Space
        # for i,num in enumerate(nums):
        #     curr = abs(num)
        #     if nums[curr-1] > 0:
        #         nums[curr-1] *= -1
        #     else:
        #         duplicate = curr

        # Way 2: To find Duplicate using Set
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                duplicate = num

        missingNum = sum([i for i in range(1, n + 1)]) - (currSum - duplicate)
        return [duplicate, missingNum]

