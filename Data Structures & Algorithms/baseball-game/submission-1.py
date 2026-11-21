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
            elif(c == "C"):
                stack.pop()
            elif(c == "D"):
                stack.append(stack[-1]*2)
            else:
                stack.append(int(c))

        for v in stack:
            res += v
        return res

