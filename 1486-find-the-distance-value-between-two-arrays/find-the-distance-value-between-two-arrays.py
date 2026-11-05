class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        count =0
        for num in arr1:
            idx=bisect.bisect(arr2,num)
            is_valid=True
            if idx < len(arr2) and abs(num - arr2[idx]) <= d:
                is_valid = False
            if idx > 0 and abs(num - arr2[idx - 1]) <= d:
                is_valid = False
        
            if is_valid:
                count += 1
    
        return count
