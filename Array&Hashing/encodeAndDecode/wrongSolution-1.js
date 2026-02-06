// WARNING: This solution is wrong because the may have similar string multiple times
const stringMap = new Map();

const encode = (strArray) => {
  for (const element of strArray) {
    stringMap.set(element, element.length);
  }
  return strArray.join("");
};

const decode = (str) => {
  let res = [];
  let start = 0;
  let end = 0;
  for (const [key, value] of stringMap) {
    end += value;
    res.push(str.slice(start, end));
    start = end;
  }
  return res;
};

// const strArray = ["Hello", "World"];
const strArray = [""]
const encodedString = encode(strArray);
const decodedArray = decode(encodedString);
console.log(decodedArray);
