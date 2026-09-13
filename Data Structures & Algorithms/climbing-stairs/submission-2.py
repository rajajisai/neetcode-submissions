class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        dp[n]=1
        def numWays(stair:int,n:int,dp:[]):
            if (stair>n):
                return 0
            if (dp[stair]>-1):
                return dp[stair]

            dp[stair]=numWays(stair+1,n,dp)+numWays(stair+2,n,dp)
            
            return dp[stair]
        
        return numWays(0,n,dp)


        