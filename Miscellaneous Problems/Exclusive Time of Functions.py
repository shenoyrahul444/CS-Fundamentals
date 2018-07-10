class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        if n == None or logs == None or logs == []:
            return []

        stack = []
        s = logs[0].split(":")
        stack.append(int(s[0]))
        prev = int(s[2])
        result = [0] * n
        i = 1
        while i < len(logs):
            s = logs[i].split(":")
            if s[1] == "start":
                result[stack[-1]] += int(s[2]) - prev
                stack.append(int(s[0]))
                prev = int(s[2])
            else:
                pid = stack.pop()
                result[pid] += int(s[2]) - prev + 1
                prev = int(s[2]) + 1
            i += 1
        return result

sol = Solution()
# print(sol.exclusiveTime(2,["0:start:0","1:start:2","1:end:5","0:end:6"]))
print(sol.exclusiveTime(1,["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))



    # Approach 2 - Complex and Not fullproof
class Solution1(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        if n == None or logs == None or logs == []:
            return []

        time_consumed = 0
        i = 1
        result = [0] * n
        rpid, rstatus, rtime = logs[0].split(":")
        rpid, rtime = int(rpid), int(rtime)

        while i < len(logs):
            pid, status, time = logs[i].split(":")
            pid, time = int(pid), int(time)
            if status == "start":
                time_consumed += time - rtime if rtime == 0 else time - rtime + 1
                i, rtime = self.handleCall(logs, i, result)
                i += 1
            elif pid == rpid:
                time_consumed += time - rtime
                result[pid] += time_consumed
                return result

    def handleCall(self, logs, i, result):

        rpid, rstatus, rtime = logs[i].split(":")
        rpid, rtime = int(rpid), int(rtime)
        time_consumed = 0
        i += 1
        while i < len(logs):
            pid, status, time = logs[i].split(":")
            pid, time = int(pid), int(time)
            if status == "start":
                time_consumed += time - rtime if rtime == 0 else time - rtime + 1
                i, rtime = self.handleCall(logs, i, result)
                i += 1
            elif pid == rpid:
                time_consumed += time - rtime
                result[pid] += time_consumed
                return i, time


sol = Solution1()
# print(sol.exclusiveTime(2,["0:start:0","1:start:2","1:end:5","0:end:6"]))
# print(sol.exclusiveTime(1,["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))