"""Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

In case of multiple subarrays, return the subarray which comes first on moving from left to right.

"""

class Solution:
    def subArraySum(self,arr, n, s):

        for i in range(n):
            currentSum = arr[i]

            j = i+1

            while j<=n:

                if currentSum == s:
                    print("indexes {} to {}".format(i,j-1))

                    return currentSum

                if currentSum > s:

                    break

                currentSum = currentSum + arr[j]

                j = j +1


        print("No subset found")
        return 0

n = 5
s = 12
arr = [1 ,2 ,3 ,7 ,5]
obj = Solution()
ans = obj.subArraySum(arr,n,s)
print(ans)
