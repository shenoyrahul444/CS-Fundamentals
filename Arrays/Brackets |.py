"""
Tell if the input string of brackets is Valid or Not

s1 = "(([()]))"  #   Valid
s2 = "(([()))"   #   Invalid

The string will contain 2 types of brackets. () and []
If String is valid collection of brackets, return True
"""

def isValidBrackets(s):
    if s == None:
        return False

    if s == "":
        return True

    # mapping opening an closing brackets
    stack = []
    mem = {
        ")":"(",
        "]":"["
    }

    # Approach 1 - Using Stacks
    def approach_1(s,mem):

        for ele in s:
            if ele in ["(","["]:
                stack.append(ele)
            else:
                if ele in mem:
                    if stack != []:
                        if mem[ele] == stack[-1]:
                            stack.pop()
                        else:
                            return False
                    else:
                        return False
        if stack != []:
            return False
        return True

    # Approach 2 - Using Pointers
    def approach_2(s, mem):
        p_cnt = 0
        br_cnt = 0

        for ele in s:
            if ele in ["(","]"]:
                if ele == "(":
                    p_cnt += 1
                else:
                    br_cnt += 1
            else:
                if ele in mem:
                    if p_cnt > 0 and br_cnt > 0:
                        # if mem[ele] == :
                        pass
                # This approach  doesn't work, as we need to see verify the opening bracket for the closing bracket encountered.
                # Counters do not give the information regarding the last opening element we encounter

    return approach_1(s,mem)
    # approach_2(s,mem) # Approach 2 with




ips = [ "(([()]))",  "(([()))",None,""]
ops = [True,False,False,True]
i = 1
for ip,op in list(zip(ips,ops)):
    if isValidBrackets(ip) == op:
        print("Test Case "+str(i)+" Passed")
    else:
        print("Test Case " + str(i) + " Failed")
    i+=1
# print(isValidBrackets(s1))
# print(isValidBrackets(s2))