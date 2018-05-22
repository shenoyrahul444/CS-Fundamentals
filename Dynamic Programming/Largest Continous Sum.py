# Finding the Largest Continuous Sum for a given array
class Solution:
    def largest_continuous_sum(self,arr):

        # Edge cases
        if arr == None or arr == []:
            return 0

        n = len(arr)

        if n == 1:
            return arr[0]

        current_sum = arr[0]
        max_sum = arr[0]

        for num in arr[1:]:
            current_sum = max(current_sum+num,num)
            max_sum = max(current_sum,max_sum)
            print(current_sum,max_sum)
        return max_sum


array = [1,-1,3,2,6,-3,9,2]
sol = Solution()
print(sol.largest_continuous_sum(array))


