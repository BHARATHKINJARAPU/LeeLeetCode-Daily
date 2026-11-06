class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        # Sort logs by request time
        logs.sort(key=lambda l: l[1])
        
        # Pair each query with its original index, then sort by query value
        q = sorted(enumerate(queries), key=lambda p: p[1])
        
        cnt = collections.defaultdict(int)  # server_id -> # requests inside window
        ans = [0] * len(queries)
        left = right = active = 0
        
        for idx, t in q:
            lo = t - x
            
            # Expand right edge: absorb all logs with time <= t
            while right < len(logs) and logs[right][1] <= t:
                server_id = logs[right][0]
                if cnt[server_id] == 0:
                    active += 1
                cnt[server_id] += 1
                right += 1
            
            # Shrink left edge: drop all logs with time < lo
            while left < right and logs[left][1] < lo:
                server_id = logs[left][0]
                if cnt[server_id] == 1:
                    active -= 1
                    del cnt[server_id]
                else:
                    cnt[server_id] -= 1
                left += 1
            
            ans[idx] = n - active
        
        return ans