class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numbers = set()
        for num in nums:
            if num in numbers:
                return True
            else: 
                numbers.add(num)
        return False

def main():
    solution = Solution()
    nums = [1, 1, 3, 4, 5]
    print(solution.containsDuplicate(nums))

if __name__ == "__main__":
    main()
