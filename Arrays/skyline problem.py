class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return [[]]
        x_max = 0
        for building in buildings:
            x_max = max(building[1], x_max)

        ground = [0] * (x_max + 2)
        for x, y, h in buildings:
            for wall in range(x, y + 1):
                ground[wall] = max(ground[wall], h)
        points = []
        prev_height = 0
        i = 0
        while i < (x_max+1):
            if (ground[i] != prev_height and prev_height < ground[i]):
                points.append([i, ground[i]])
                prev_height = ground[i]
            elif ground[i] > ground[i + 1]:
                points.append([i, ground[i + 1]])
                prev_height = ground[i + 1]
            i += 1
        return points



skyline = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print(Solution().getSkyline(skyline))