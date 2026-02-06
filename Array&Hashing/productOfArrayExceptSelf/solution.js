const productOfArray = (nums) => {
  const productMap = new Map();
  let product = 1;
  for (let i = 0; i < nums.length; i++) {
    product = product * nums[i];
    productMap.set(i, product);
  }
  console.log(productMap);
};

const nums = [-1, 0, 1, 2, 3];
productOfArray(nums);
