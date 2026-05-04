class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        slow = 0
        fast = len(numbers) - 1
        while slow < fast:
            if numbers[slow] + numbers[fast] > target:
                fast -= 1
                continue
            if numbers[slow] + numbers[fast] < target:
                slow += 1
                continue
            if numbers[slow] + numbers[fast] == target:
                return [slow + 1, fast + 1]