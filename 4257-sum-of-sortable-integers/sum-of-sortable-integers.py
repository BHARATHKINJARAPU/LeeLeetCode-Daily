class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n=len(nums)
        pref=[0]*n
        cur=0
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                cur+=1
            pref[i+1]=cur
        if cur==0:
            ans=0
            for d in range(1,int(n**0.5)+1):
                if n%d==0:
                    ans+=d
                    if d*d!=n:
                        ans+=n//d
            return ans
        last_drop=[0]*n
        last=-1
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                last=i
            last_drop[i+1]=last
        divisors = []
        for d in range(1, int(n**0.5) + 1):
            if n % d == 0:
                divisors.append(d)
                if d * d != n:
                    divisors.append(n // d)
        ans = 0
        for k in divisors:
            if k == 1:
                continue
                
            valid = True
            prev_max = -1
            
            for l in range(0, n, k):
                r = l + k - 1
                num_drops = pref[r] - pref[l]
                
                if num_drops == 0:
                    cur_min = nums[l]
                    cur_max = nums[r]
                elif num_drops == 1 and nums[r] <= nums[l]:
                    idx = last_drop[r]
                    cur_min = nums[idx + 1]
                    cur_max = nums[idx]
                else:
                    valid = False
                    break
                    
                if cur_min < prev_max:
                    valid = False
                    break
                prev_max = cur_max
                
            if valid:
                ans += k
                
        return ans
