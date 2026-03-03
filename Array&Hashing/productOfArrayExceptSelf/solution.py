def solution(nums):
  n = len(nums)
  res = [1] * n
  prefix = 1
  for i in range(1, n):
    prefix *= nums[i-1]
    res[i] = prefix
  postfix = 1
  for i in range(n-1, -1, -1):
    res[i] *=postfix
    postfix = postfix * nums[i]
  return res



answer = solution([2,4,6,0,2,10,9])
print(answer)
