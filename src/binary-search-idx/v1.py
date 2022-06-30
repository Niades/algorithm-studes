import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print("* search() called")
        if len(nums) == 0:
            return -1;
        resultIdx = 0
        middleIdx = math.floor(len(nums) / 2)
        middle = nums[middleIdx]

        recurResultIdx = - 1
        print("nums = ", nums)
        print("target = ", target)
        print('middleIdx = ', middleIdx)
        print('middle = ', middle)
        print('target = ', target)
        
        if nums[middleIdx] == target:
            print('found the target')
            resultIdx = 0
            print('* 1 final resultIdx = ', resultIdx)
            return resultIdx
        elif target >= middle:
            print('going right')
            recurResultIdx = self.search(nums[middleIdx + 1:], target)
            print("recurResultIdx = ", recurResultIdx)
            print('middleIdx = ', middleIdx)
            print('resultIdx = ', resultIdx)
            resultIdx += middleIdx - recurResultIdx
            print("resultIdx += middleIdx - recurResultIdx = ", resultIdx)
        elif target <= middle:
            print('going left')
            recurResultIdx = self.search(nums[:middleIdx], target)
            print("recurResultIdx = ", recurResultIdx)
            print('middleIdx = ', middleIdx)
            print('resultIdx = ', resultIdx)
            resultIdx += middleIdx + recurResultIdx
            print("resultIdx += middleIdx + recurResultIdx = ", resultIdx)
            
        if resultIdx < 0:
            print('* 2 final resultIdx = ', resultIdx)
            resultIdx = - 1
        # Adjust resultIdx by 1:
        if len(nums) != 1:
            print('* Adjusting the result by +1 ')
            resultIdx += 1
        print('* 3 final resultIdx = ', resultIdx)
        return resultIdx