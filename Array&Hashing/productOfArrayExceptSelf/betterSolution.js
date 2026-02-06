//This solution uses division method
const productOfArray = (nums) => {
  let zeros = 0;
  let prod = 1;
  const res = [];
  
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === 0) {
      zeros++;
    } else {
      prod *= nums[i];
    }
  }

  for (let i = 0; i < nums.length; i++) {
    if (zeros === 1) {
      if (nums[i] === 0) {
        res[i] = prod;
      } else {
        res[i] = 0;
      }
    } else if (zeros > 1) {
      res[i] = 0;
    } else {
      res[i] = prod / nums[i];
    }
  }

  return res;
};

const nums = [1, 2, 4, 6];
const result = productOfArray(nums);
console.log(result);
