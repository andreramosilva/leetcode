class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        total = 0
        heap1 = []
        heap2 = []
        n = len(costs)
        left = 0
        right = n -1
        for _ in range(k):
            i = 0
            while len(heap1) < candidates and left <= right:
                heappush(heap1,costs[left])
                left+=1
            while len(heap2) < candidates and left <=right:
                heappush(heap2,costs[right])
                right-=1
            
            l = heap1[0] if heap1 else maxsize
            r = heap2[0] if heap2 else maxsize

            if l <= r:
                total+=l
                heappop(heap1)
            else:
                total+=r
                heappop(heap2)

        return total