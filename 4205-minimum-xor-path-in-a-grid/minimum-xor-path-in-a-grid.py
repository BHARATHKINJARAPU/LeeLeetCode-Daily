class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[j] is an integer bitmask where the k-th bit is 1 
        # if XOR sum 'k' is reachable at column j.
        dp = [0] * n
        dp[0] = 1 << grid[0][0]
        
        # 1. Fill the first row (only moves from the left)
        for j in range(1, n):
            val = grid[0][j]
            prev_mask = dp[j - 1]
            cur_mask = 0
            # Iterate only through set bits in prev_mask
            while prev_mask:
                lsb = prev_mask & -prev_mask
                k = lsb.bit_length() - 1
                cur_mask |= 1 << (k ^ val)
                prev_mask ^= lsb
            dp[j] = cur_mask
            
        # 2. Process the remaining rows
        for i in range(1, m):
            # First column (can only move from the cell above)
            val0 = grid[i][0]
            prev_mask0 = dp[0]
            cur_mask0 = 0
            while prev_mask0:
                lsb = prev_mask0 & -prev_mask0
                k = lsb.bit_length() - 1
                cur_mask0 |= 1 << (k ^ val0)
                prev_mask0 ^= lsb
            dp[0] = cur_mask0
            
            # Other columns (can move from the cell above OR the cell to the left)
            for j in range(1, n):
                val = grid[i][j]
                combined = dp[j] | dp[j - 1]
                cur_mask = 0
                while combined:
                    lsb = combined & -combined
                    k = lsb.bit_length() - 1
                    cur_mask |= 1 << (k ^ val)
                    combined ^= lsb
                dp[j] = cur_mask
                
        # 3. Find the lowest set bit in the destination cell (m - 1, n - 1)
        target_mask = dp[n - 1]
        lowest_set_bit = target_mask & -target_mask
        return lowest_set_bit.bit_length() - 1