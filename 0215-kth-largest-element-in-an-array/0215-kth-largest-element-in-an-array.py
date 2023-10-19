class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # result = sorted(nums)
        # result.reverse()
        # return result[k-1]
        max_heap = []
        result = None
        for val in nums:
            heappush(max_heap,-1 * val)
        for i in range(k):
            result = heappop(max_heap)
        return result * -1