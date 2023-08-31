class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_nums = {}
        for l,n in enumerate(nums):
            dif = target - n
            if dif in map_nums:
                return [map_nums[dif],l]
            else:
                map_nums[n]=l    
        return