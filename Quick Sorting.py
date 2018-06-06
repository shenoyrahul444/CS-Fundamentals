class Solution:
    def sortArray(self,arr):

        n = len(arr)
        self.quickSort(arr,0,n-1)
    def quickSort(self,arr,low,high):
        if low<high:

            pivot = self.partition(arr,low,high)

            self.quickSort(arr,low,pivot-1)
            self.quickSort(arr,pivot+1,high)
    def partition(self,arr,low,high):
        if low<high:
            i = (low - 1)
            pivot = arr[high]
            for j in range(low,high):
                if arr[j] <= pivot:
                    i+=1
                    arr[i],arr[j] = arr[j],arr[i]

            arr[i+1],arr[high] = arr[high],arr[i+1]
        return (i+1)

sol = Solution()
arr = [5,2,4,5,1,3,34,2,4,9]
print(arr)
sol.sortArray(arr)
print(arr)


