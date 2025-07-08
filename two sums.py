def two_sums(number,target):
    seen = {}
    for i, nums in enumerate(number):
        needed = target - nums
        if needed in seen:
           return [seen[needed],i]

        seen[nums] = i


print(two_sums([2,3,4,7],9))



