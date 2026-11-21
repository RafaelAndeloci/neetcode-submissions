class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for idx,c in enumerate(operations):
            if(c == "+"):
                second = stack.pop()
                first = stack.pop()
                stack.append(first)
                stack.append(second)
                stack.append(first + second)
                res += first + second
            elif(c == "C"):
                res -= stack.pop()
            elif(c == "D"):
                res += stack[-1] * 2
                stack.append(stack[-1]*2)
            else:
                stack.append(int(c))
                res += int(c)

        return res

