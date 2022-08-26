a = [1,2,4,5,8,9]
target = 6

#time complexity O(n^2)
#space complexity O(n^2)
def two_sum_brute_f(a,target):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i]+a[j]==target:
                print(a[i],a[j])
                return True
    return False

print(two_sum_brute_f(a,target))

# Time complexity 0(n)
# space comletciy O(n)


def two_sum_using_ht(a,target):
    ht = {} #initating hastable
    for i in range(len(a)):
        if a[i] in ht:
            print(ht[a[i]],a[i])
        else:
            ht[target-a[i]]=a[i]
            return False
print(two_sum_using_ht(a,target))

# Time Complexity: O(n)
# Space Complexity: O(1)
def two_sum(a, target):
    i = 0
    j = len(a) - 1
    while i < j:
        if a[i] + a[j] == target:
            print(a[i], a[j])
            return True
        elif a[i] + a[j] < target:
            i += 1
        else:
            j -= 1
    return False

print(two_sum(a,target))
