// Arrays can be used as stacks
const arr = [1, 2, 3];
arr.push(4);
arr.push(5);
// console.log(arr);

arr.pop();
// console.log(arr);

//add elements at front(Mutable: changes the original array)
arr.unshift(6, 7, 8);
console.log(arr); //[6, 7, 8 , 1, 2, 3]

//add elements at front using spread operator(Immutable: does not change the original array)
const newValue = 9;
const newArray = [newValue, ...arr];
console.log(newArray);

//Elements can be added at the front using concat() method
