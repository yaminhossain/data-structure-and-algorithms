//=========================== recheck =======================

const frequentElements = (numbers, k) => {
  const frequencyMap = new Map();
  for (const num of numbers) {
    frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1);
  }

  let temp = [];
  for (const [key, value] of frequencyMap) {
    temp.push([value, key]);
  }

  let res = [];
  for (const elem of temp.sort((a, b)=> b[1] - a[1]).slice(0, k)) {
    res.push(elem[1]);
  }
  return res;
};

const nums = [1, 2, 2, 3, 3, 3, 3];
const k = 2;
const res = frequentElements(nums, k);
console.log("Result", res);
