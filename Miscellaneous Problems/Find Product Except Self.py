class Solution1(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
        Time complexity 
        -> O(n)

        Space Complexit (Excluding the output list)
        -> 2* O(n)         
        """
        # Checking edge cases
        if nums == None or nums == []:
            return []
        n = len(nums)

        # Creating Left, Right and Output Lists of length 'n'
        left = [1] * n  # left list
        right = [1] * n  # right list
        output = [1] * n  # output list

        # Updating left list with the product of the left elements
        temp = 1
        for i in range(n):
            left[i] *= temp
            temp *= nums[i]

        # Updating right list with the product of the right elements
        temp = 1
        for i in range(n - 1, -1, -1):
            right[i] *= temp
            temp *= nums[i]

        # Updating output list with the product of left[i] and right[i]
        for i in range(n):
            output[i] = left[i] * right[i]

        # Returning output list
        return output


sol = Solution1()
arr1 = [1,5,6,2,7,9]
arr2 = [1,-1]
arr3 = [0,1,2,3]
# print(sol.productExceptSelf(arr1)) # Input = [1,5,6,2,7,9]       Output = [3780, 756, 630, 1890, 540, 420]
# print(sol.productExceptSelf(arr2)) # Input = [1,-1]              Output = [-1, 1]
# print(sol.productExceptSelf(arr3)) # Input = [0,1,2,3]           Output = [6, 0, 0, 0]

" This code has been contributed by Rahul Shenoy "


class Solution2(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
        Time complexity 
        -> O(n)

        Space Complexit (Excluding the output list)
        -> 2* O(n)         
        """
        # Checking edge cases
        if nums == None or nums == []:
            return []
        n = len(nums)

        # Creating Left, Right and Output Lists of length 'n'
        output = [1] * n  # output list

        # Updating output list with the product of the left elements
        temp = 1
        for i in range(n):
            output[i] *= temp
            temp *= nums[i]

        # Updating output list with the product of the left and right elements
        temp = 1
        for i in range(n - 1, -1, -1):
            output[i] *= temp
            temp *= nums[i]

        # Returning output list
        return output


sol = Solution2()
arr1 = [1,5,6,2,7,9]
arr2 = [1,-1]
arr3 = [0,1,2,3]
print(sol.productExceptSelf(arr1)) # Input = [1,5,6,2,7,9]       Output = [3780, 756, 630, 1890, 540, 420]
print(sol.productExceptSelf(arr2)) # Input = [1,-1]              Output = [-1, 1]
print(sol.productExceptSelf(arr3)) # Input = [0,1,2,3]           Output = [6, 0, 0, 0]

" This code has been contributed by Rahul Shenoy "