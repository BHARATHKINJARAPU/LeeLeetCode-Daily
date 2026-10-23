class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans=-1
        for i,val in enumerate(nums):
            if val!=i:
                if ans==-1:
                    ans=val
                else:
                    ans&=val
                    if ans==0:
                        return 0
        return 0 if ans==-1 else ans