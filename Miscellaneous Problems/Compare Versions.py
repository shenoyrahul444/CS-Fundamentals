"""

Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Example 2:

Input: version1 = "1.0.1", version2 = "1"
Output: 1
Example 3:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1

"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if version1 == None or version2 == None or version1 == "" or version2 == "":
            return None
        nums1 = nums2 = []

        if version1.find(".") != -1:
            nums1 = list(map(int, version1.split(".")))
        else:
            nums1 = [int(version1)]
        if version2.find(".") != -1:
            nums2 = list(map(int, version2.split(".")))
        else:
            nums2 = [int(version2)]

        n1 = len(nums1)
        n2 = len(nums2)
        if n1 == 1 and n2 == 1:
            if nums2[0] > nums1[0]:
                return -1
            elif nums2[0] < nums1[0]:
                return 1
            else:
                return 0

        for i in range(max(n1, n2)):
            if i < n1 and i < n2:
                if nums1[i] > nums2[i]:
                    return 1
                elif nums1[i] < nums2[i]:
                    return -1
            elif i < n2:
                if nums2[i] > 0:
                    return -1
            else:
                if nums1[i] > 0:
                    return 1
        return 0


sol = Solution()
v1 = "1.2.3"
v2 = "1.2.3.0"
print(sol.compareVersion(v1,v2))