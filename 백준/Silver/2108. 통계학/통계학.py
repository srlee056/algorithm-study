import sys

n = int(sys.stdin.readline())

nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()

avg = sum(nums)/len(nums)
if avg >=0:
    print(int(avg+0.5))
else:
    print(int(avg-0.5))
print(nums[n//2])

num_dict = {}
for num in nums:
    num_dict[num] = num_dict.get(num, 0) + 1

sort_by_count = sorted(num_dict.items(), key=lambda x : x[1], reverse=True)
#print(sort_by_count)

if len(sort_by_count) >= 2 and sort_by_count[0][1] == sort_by_count[1][1]:
    print(sort_by_count[1][0])
else:
    print(sort_by_count[0][0])

print(nums[-1]-nums[0])