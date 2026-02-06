def productOfArray(nums):
  output=[]
  for i in range(len(nums)):
    product = 1
    for j in range(len(nums)):
      if (i == j):
        continue
      product = product * nums[j]
    output.append(product)
  return output

nums = [-1,0,1,2,3]
result = productOfArray(nums)
print(result)

# TC: O(n^2)
# SC: O(n)