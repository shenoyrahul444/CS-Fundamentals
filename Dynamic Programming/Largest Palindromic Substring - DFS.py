class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == None:
            return ""
        s = s.strip()
        if s.strip() == "":
            return ""

        if len(s) == 1:
            return s
        maxlen = 1
        start = 0
        end = 0
        for i, char in enumerate(s):

            # checking odd palindrome pattern
            j, k = i - 1, i + 1
            curr_len = 1
            while j >= 0 and k < len(s) :
                if s[j] == s[k]:
                    curr_len += 2
                    if curr_len > maxlen:
                        start = j
                        end = k
                        maxlen = curr_len
                    j -= 1
                    k += 1

                else:
                    break
            # Checking even palindrome pattern

            if i + 1 < len(s):
                if s[i] == s[i + 1]:
                    curr_len = 2
                    j, k = i - 1, i + 2
                    while j >= 0 and k < len(s) :
                        if s[j] == s[k]:
                            curr_len += 2
                            if curr_len > maxlen:
                                start = j
                                end = k
                                maxlen = curr_len
                            k += 1
                            j -= 1

                        else:
                            break
        return s[start:end+1]



sol = Solution()
print(sol.longestPalindrome("babaddabab"))