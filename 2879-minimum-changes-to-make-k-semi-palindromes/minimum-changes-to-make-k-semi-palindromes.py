class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        divs = [[] for _ in range(n + 1)]
        for d in range(1, n):
            for length in range(2 * d, n + 1, d):
                divs[length].append(d)

        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = length
                for d in divs[length]:
                    changes = 0
                    for rem in range(d):
                        l, r = i + rem, j - d + 1 + rem
                        while l < r:
                            if s[l] != s[r]:
                                changes += 1
                            l += d
                            r -= d
                    if changes < best:
                        best = changes
                cost[i][j] = best

        INF = 10**9
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for end in range(2 * parts, n + 1):
                for start in range(2 * (parts - 1), end - 1):
                    val = dp[start][parts - 1] + cost[start][end - 1]
                    if val < dp[end][parts]:
                        dp[end][parts] = val

        return dp[n][k]