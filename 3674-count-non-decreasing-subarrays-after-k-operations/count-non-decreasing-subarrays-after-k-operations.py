from collections import deque
from typing import List


class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        cost = 0
        r = n - 1
        dq = deque()

        for l in range(n - 1, -1, -1):
            curr = nums[l]
            cnt = 1

            while dq and dq[-1][0] <= curr:
                prev_val, prev_cnt = dq.pop()
                cost += prev_cnt * (curr - prev_val)
                cnt += prev_cnt

            dq.append([curr, cnt])

            while cost > k:
                cost -= dq[0][0] - nums[r]
                dq[0][1] -= 1
                if dq[0][1] == 0:
                    dq.popleft()
                r -= 1

            ans += r - l + 1

        return ans
        