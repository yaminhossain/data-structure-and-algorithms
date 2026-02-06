// Initialize an array with default value with fixed size
// You can initialize an array with default values and a fixed size in JavaScript using the "Array() constructor" with a specific length, followed by the "fill()" method.


// Creates an array of size 5, with each element set to 0
const arr1 = new Array(5).fill(0);

console.log(arr1);
// Output: [0, 0, 0, 0, 0]
console.log("Length of arr1: ", arr1.length);

// Creates an array of size 3, with each element set to "default"
const arr2 = new Array(3).fill("default");

console.log(arr2);
// Output: ["default", "default", "default"]
console.log("Length of arr2: ", arr2.length);