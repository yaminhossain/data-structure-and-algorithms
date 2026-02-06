// Create an empty Set
const mySet = new Set();

// Create a Set from an array (duplicates are automatically removed)
const numbers = [2, 13, 4, 4, 2, 13];
const uniqueNumbers = new Set(numbers);
console.log(uniqueNumbers); // Output: Set {2, 13, 4}

// Convert a Set back to an Array using spread syntax
const uniqueArray = [...uniqueNumbers];
console.log(uniqueArray); // Output: [2, 13, 4]

//Using an array aka tuple as element
const testSet = new Set();
testSet.add([1, 2]);
testSet.add([7, 8]);
console.log("Test set: ", testSet); // { [ 1, 2 ], [ 7, 8 ] }
