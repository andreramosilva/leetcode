class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) -1
        if len(nums) < 3:
            print(max(nums))

        while left < right:
            mid = (left + right) //2
            if nums[mid] < nums[mid+1]:
                left=mid+1
            else:
                right = mid
            # mid = left + (right - left) // 2


            # if nums[mid]>nums[mid-1]and nums[mid] > nums[mid+1]:
            #     return mid
            # elif nums[mid] > nums[mid+1]:
            #     right = mid - 1
            # else:
            #     left = mid + 1
        return left