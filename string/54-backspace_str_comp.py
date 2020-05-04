# Algorithm
#
# Iterate through the string in reverse. If we see a backspace character, the next non-backspace character is skipped. If a character isn't skipped, it is part of the final answer.
#
# See the comments in the code for more details.


class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))


class Solution(object):
    def backspaceCompare(self, S, T):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)


class MySolution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        st1 = []
        st2 = []
        n = len(S)
        m = len(T)
        for i in range(n):
            if S[i] != "#":
                st1.append(S[i])
            else:
                if st1:
                    st1.pop()

        for i in range(m):
            if T[i] != "#":
                st2.append(T[i])
            else:
                if st2:
                    st2.pop()

        return st1 == st2
