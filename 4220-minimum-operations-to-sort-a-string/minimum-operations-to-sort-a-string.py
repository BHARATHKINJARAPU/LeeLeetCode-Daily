class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        if all(s[i]<=s[i+1] for i in range(n-1)):
            return 0
        if n<=2:
            return -1
        mini=min(s)
        maxi=max(s)
        if s[-1]>=max(s[:-1]) or s[0]<=min(s[1:]):
            return 1
        ismin=(s[-1]==mini and min(s[:-1])>mini)
        ismax=(s[0]==maxi and max(s[1:])<maxi)
        if ismin and ismax:
            return 3
        return 2        