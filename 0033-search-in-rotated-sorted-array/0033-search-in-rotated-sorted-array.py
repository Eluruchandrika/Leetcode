class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while nums[right]<nums[left]:
            left+=1
        if target > nums[-1]:
            right=left-1
            left=0

        while left<=right:
            mid=(left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left =mid+1
        return -1 