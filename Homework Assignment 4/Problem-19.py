class Solution:
    def isSubset(self, a, b):
        freq = {}

        for x in a:
            freq[x] = freq.get(x, 0) + 1

        for x in b:
            if x not in freq or freq[x] == 0:
                return False
            freq[x] -= 1

        return True


a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]

obj = Solution()
print(obj.isSubset(a, b))
