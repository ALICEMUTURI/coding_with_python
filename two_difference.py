def two_difference (number, target):
    seen = {}
    for i, nums in enumerate(number):
        needed = nums - target
        if needed in seen:
            return [seen[needed],i]
        seen[nums] = i

print(two_difference([3,4,5,6],2))
print(two_difference([3,4,5,6],3))