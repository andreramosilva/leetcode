class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans = 0
        n = len(costs)
        q = []
        qq = []
        l, r = 0, n - 1

        for _ in range(k):
            while len(q) < candidates and l <= r: heappush(q, costs[l]); l+=1
            while len(qq) < candidates and l <= r: heappush(qq, costs[r]); r-=1

            a = q[0] if q else maxsize
            b = qq[0] if qq else maxsize

            if a <= b: ans += a; heappop(q)
            else: ans += b; heappop(qq)
        return ans 