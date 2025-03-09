#Generate Binary Strings
N = int(input())
for i in range(2**N):
    print(bin(i)[2:].zfill(N))


class Solution:
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generateStrings(result, [], n, -1)
        return result

    def generateStrings(self, result, sb, n, lastChar):
        if len(sb) == n:
            result.append(''.join(sb))
            return

        # Add '1' to the string
        sb.append('1')
        self.generateStrings(result, sb, n, 1)
        sb.pop()

        # Add '0' to the string, only if the last character was not '0'
        if lastChar != 0:
            sb.append('0')
            self.generateStrings(result, sb, n, 0)
            sb.pop()
            
def bubbleSort(nums, k):
    swaps = 0
    n = len(nums)
    
    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swaps += 1
                if swaps > k:
                    return False
    return True