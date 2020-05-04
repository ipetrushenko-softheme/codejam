# don't work for 3 + 2*4/3
#class Solution:
#
#    def calculate(self, s: str) -> int:
#        if '+' in s:
#            idx = s.rfind('+')
#            return self.calculate(s[:idx]) + self.calculate(s[idx + 1:])
#        elif '-' in s:
#            idx = s.rfind('-')
#            return self.calculate(s[:idx]) - self.calculate(s[idx + 1:])
#        elif '*' in s:
#            idx = s.rfind('*')
#            return self.calculate(s[:idx]) * self.calculate(s[idx + 1:])
#        elif '/' in s:
#            idx = s.rfind('/')
#            return self.calculate(s[:idx]) // self.calculate(s[idx + 1:])
#        else:
#            return int(s)
#


class Solution:

    # def read_num(self, idx: int, s: str) -> int:
    #     num = ''
    #     while idx < len(s) and s[idx].isdigit():
    #         num += s[idx]
    #         idx = idx + 1
    #     return num
#
    # def apply(self, first: int, second: int, op: str) -> int:
    #     if op == "+":
    #         return first + second
    #     if op == "-":
    #         return first - second
    #     if op == "*":
    #         return first * second
    #     if op == "/":
    #         return first // second
#
    #     raise Exception("unknown op")

    def calculate(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        res, num = 0, 0
        sign = '+'
        stack = []
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if (not s[i].isdigit() and s[i] != " ") or i == len(s) - 1:
                if sign == '-':
                    stack.append(-num)
                if sign == '+':
                    stack.append(num)
                if sign == '*':
                    product = stack.pop() * num
                    stack.append(product)
                if sign == '/':
                    quotient = stack.pop() / num
                    stack.append(int(quotient))
                sign = s[i]
                num = 0
        while stack:
            res += stack.pop()
        return res


s = Solution()
print(s.calculate("1+2*5/3+6/4*2"))
print(s.calculate(" 3/2 "))
print(s.calculate(" 3+5 / 2 "))
print(s.calculate("42"))
print(s.calculate("0-2147483647"))
print(s.calculate("1-1+1"))
print(s.calculate("1+1-1"))
