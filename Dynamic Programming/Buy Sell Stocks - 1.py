"""Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
ans = [15,20]
# ans.insert(0,5)
# ans.append([5])
# print(ans)
ans.extend([5])
print(ans)
# name = []
# name.append([])
# print(name)
# name.append([1])
# print(name)
# name.append([1])
# print(name)



while curr:
                if curr.left and curr.right:
                    curr.left.next = curr.right
                    temp = curr.right
                elif curr.right:
                    temp = curr.right
                elif curr.left:
                    temp = curr.left
                if leftmost == None:
                    if curr.left:
                        leftmost = curr.left
                    elif curr.right:
                        leftmost = curr.right
                if temp and curr.next:
                    if curr.next.left:
                        temp.next = curr.next.left
                        temp = None
                    elif curr.next.right:
                        temp.next = curr.next.right
                        temp = None
                curr = curr.next