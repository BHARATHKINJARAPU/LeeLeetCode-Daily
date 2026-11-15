from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        even_count = 1
        odd_count = 0
        prefix_parity = 0
        ans = 0

        for num in arr:
            prefix_parity ^= num & 1
            if prefix_parity:
                ans += even_count
                odd_count += 1
            else:
                ans += odd_count
                even_count += 1

        return ans % MOD