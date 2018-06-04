class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        if source == None or source == []:
            return source

        block_started = False
        result = []
        sentence = ""
        for line in source:
            n = len(line)
            i = 0
            while i < n:
                if i + 1 < n and (line[i] == "/" and line[i + 1] == "*") or (line[i] == "*" and line[i + 1] == "/"):
                    block_started = not block_started
                    i += 2
                elif block_started == False:
                    if i + 1 < n and line[i] == "/" and line[i + 1] == "/":
                        break
                    sentence += line[i]
                    i += 1

            if len(sentence) > 0 and block_started == False:
                result.append(sentence)
                sentence = ""
        if len(sentence) > 0:
            result.append(sentence)
        return result



