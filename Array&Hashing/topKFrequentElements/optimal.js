const frequentElement = (numbers, k) => {
  const freq = new Map();

  for (const num of numbers) {
    freq.set(num, (freq.get(num) || 0) + 1);
  }

  return [...freq.entries()]
    .sort((a, b) => b[1] - a[1])
    .slice(0, k)
    .map(([num]) => num);
};
const nums = [1, 2, 2, 3, 3, 3, 3];
const k = 2;
const res = frequentElement(nums, k);
console.log("Result", res);
