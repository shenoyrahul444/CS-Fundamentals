"""

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == [] or nums == None:
            return []
        if len(nums) == 1:
            return nums
        result = []
        n = len(nums)
        for i in range(n):
            for seq in self.permute(nums[:i] + nums[i + 1:]):
                if type(seq) == list:
                    result.append([nums[i]]+ seq)
                else:
                    result.append([nums[i]] + [seq])
        return result

sol = Solution()
print(sol.permute([1,2,3]))