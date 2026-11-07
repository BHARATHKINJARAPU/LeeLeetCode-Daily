class Solution:
    import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)
        
        # Min-heap of (weight, index) for free servers
        free = [(servers[i], i) for i in range(n)]
        heapq.heapify(free)
        
        # Min-heap of (free_time, weight, index) for busy servers
        busy = []
        ans = []
        
        # Current time: must track even if we skip ahead
        t = 0
        
        for j in range(len(tasks)):
            # At time j, the new task arrives.
            # But we may need to jump time if no free servers.
            
            # Release servers that are free at time max(t, j)
            release_time = max(t, j)
            
            while busy and busy[0][0] <= release_time:
                _, weight, idx = heapq.heappop(busy)
                heapq.heappush(free, (weight, idx))
            
            if free:
                # Assign immediately
                weight, idx = heapq.heappop(free)
                heapq.heappush(busy, (release_time + tasks[j], weight, idx))
                ans.append(idx)
                t = release_time
            else:
                # No free servers — jump to the earliest free time
                free_time, weight, idx = heapq.heappop(busy)
                heapq.heappush(free, (weight, idx))
                
                # Release all servers that become free at that same time
                while busy and busy[0][0] == free_time:
                    ft, w, i = heapq.heappop(busy)
                    heapq.heappush(free, (w, i))
                
                weight, idx = heapq.heappop(free)
                heapq.heappush(busy, (free_time + tasks[j], weight, idx))
                ans.append(idx)
                t = free_time
        
        return ans