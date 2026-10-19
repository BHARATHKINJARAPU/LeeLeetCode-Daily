class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        countsm = sum(1 for num in nums if num < target)
        countlr = sum(1 for num in nums if num == target)
        
        return list(range(countsm, countsm + countlr))
        