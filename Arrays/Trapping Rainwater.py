class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height == None or height == []:
            return 0
        n = len(height)

        water = 0
        i = 0
        while i < n-1:
            h1 = height[i]
            if h1 == 0:
                i+=1
            else:
                j = i + 1
                next_tallest = -1
                while j < n:
                    h2 = height[j]
                    if h2 >= h1:
                        if j > i+1:
                            water += (h1 - next_tallest) * (j-i-1)
                        break
                    elif h2<h1:
                        if next_tallest == -1:
                            next_tallest = h2
                        elif h2 > next_tallest:
                            water += (h2-next_tallest)*(j-i-1)
                            next_tallest = h2

                    j+=1
                i+=1
        return water

sol = Solution()
arr =[0,1,0,2,1,0,1,3,2,1,2,1]

print(sol.trap(arr))