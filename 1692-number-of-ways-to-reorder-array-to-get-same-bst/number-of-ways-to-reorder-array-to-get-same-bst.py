class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        mod=10**9+7
        n=len(nums)
        fact=[1]*(n+1)
        for i in range(1,n+1):
            fact[i]=fact[i-1]*i%mod
        inv_fact=[1]*(n+1)
        inv_fact[n]=pow(fact[n],mod-2,mod)
        for i in  range(n,0,-1):
            inv_fact[i-1]=inv_fact[i]*i%mod
        def comb(a:int,b:int)->int:
            if b<0 or b>a:
                return 0
            return fact[a]*inv_fact[b]%mod*inv_fact[a-b]%mod
        def ways(arr):
            m=len(arr)
            if m<=2:
                return 1
            root=arr[0]
            left=[x for x in arr[1:] if x<root]
            right=[x for x in arr[1:] if x>root]
            return comb(m-1,len(left))*ways(left)%mod*ways(right)%mod
        return (ways(nums)-1)%mod