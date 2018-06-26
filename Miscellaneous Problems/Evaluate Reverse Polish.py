"""


Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

"""

import math


class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if tokens == None:
            return

        if len(tokens) == 1:
            return int(tokens[0])

        if len(tokens) < 3:
            return list(map(int, tokens))

        stack = []

        for element in tokens:
            if element in ["*", "/", "+", "-"]:
                res = None
                if len(stack) >= 2:
                    operand2 = int(stack.pop())
                    operand1 = int(stack.pop())

                    if element == "*":
                        res = operand1 * operand2
                        res = math.floor(res) if res > 0 else math.ceil(res)
                    elif element == "/":
                        res = operand1 / operand2
                        res = math.floor(res) if res > 0 else math.ceil(res)
                    elif element == "+":
                        res = operand1 + operand2
                    elif element == "-":
                        res = operand1 - operand2
                    stack.append(res)
            else:
                stack.append(element)
        return stack[0]


sol = Solution()
print(sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))