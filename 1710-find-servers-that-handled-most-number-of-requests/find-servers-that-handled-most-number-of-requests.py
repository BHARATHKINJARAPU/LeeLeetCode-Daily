from heapq import heappush, heappop

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = list(range(k))
        busy = []
        counts = [0] * k

        for i, (start, duration) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, server_id = heappop(busy)
                heappush(available, i + (server_id - i) % k)

            if available:
                server_id = heappop(available) % k
                counts[server_id] += 1
                heappush(busy, (start + duration, server_id))

        max_requests = max(counts)
        return [s for s, count in enumerate(counts) if count == max_requests]