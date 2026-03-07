i = 0
while i < 5:
    print("hello")
    i += 1
print(i)

n = 3
j = 1
while j <= 10:
    print(n * j)
    j += 1
    
k = 0
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
while k <= len(nums) - 1:
    print(nums[k])
    k += 1
    
no = 25
idx = 0
while idx <= len(nums) - 1:
    if (nums[idx] == no):
        print(idx)
        break
    idx += 1
    
a = 1
while a <= 10:
    if (a%2 == 0):
        a += 1
        continue
    print(a)
    a += 1