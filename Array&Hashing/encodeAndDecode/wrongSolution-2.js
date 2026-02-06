// WARNING: This solution is wrong because the encoding and decoding depends on global array.
//Decoder only decodes from only the string sent to the decoder without relying on array.

const strLengths = [];
const encode = (strArr) => {
  for (let i = 0; i < strArr.length; i++) {
    strLengths.push(strArr[i].length);
  }

  return strArr.join("");
};

const decode = (joinedStrings) => {
  const res = [];
  let start = 0;
  let end = 0;

  for (const len of strLengths) {
    if (len == 0) {
      res.push("");
    } else {
      end = start + len;
      res.push(joinedStrings.slice(start, end));
      start = end;
    }
  }
  return res;
};

const dummyInput = [""];
const joinedStrings = encode(dummyInput);
const result = decode(joinedStrings);
console.log(result);
