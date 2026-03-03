# This method uses prefix and postfix method
def productOfArray(nums):
  n = len(nums)
  prefixProd = []
  postfixProd = [0]*n
  res = []

  product = 1
  # Calculating prefix products
  for i in range(n):
    product *= nums[i]
    prefixProd.append(product)
  product = 1
  # Calculating postfix products
  for i in range(n-1, -1, -1):
    product *= nums[i]
    postfixProd[i] = product
  # Calculating products of element except self
  for i in range(n):
    prod = 1
    if(i == 0):
      prod = 1 * postfixProd[i+1]
    elif(i == n-1):
      prod = prefixProd[i-1] * 1
    else:
      prod = prefixProd[i-1] * postfixProd[i+1]
    res.append(prod)
  return res



nums = [-1,0,1,2,3]
res = productOfArray(nums)
print("Result: ", res)

# TC: O(n)
# SC: O(n)