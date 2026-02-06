//We can sort an array using sort() method

const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.sort();
console.log("Fruits: ", fruits);

//reverse sorting
const arr = [5, 4, 7, 3, 8];
arr.sort().reverse();
console.log("Arr: ", arr);

/* =============================================================================================
                                        Custom sorting
To memorize this, remember that (a, b) => a - b sorts numbers in ascending order.
=================================================================================================*/

//Ascending Order
const numbers = [100, 20, 5, 42];
numbers.sort((a, b) => a - b);
console.log(numbers); // Result: [5, 20, 42, 100]

//Descending Order
const numbers2 = [100, 20, 5, 42];
numbers.sort((a, b) => b - a);
console.log(numbers2); // Result: [100, 42, 20, 5]

//array of objected by properties
const users = [
  { name: "Bob", age: 30 },
  { name: "Alice", age: 25 },
  { name: "Charlie", age: 35 },
];

// Sort by age in ascending order
users.sort((a, b) => a.age - b.age);

/* Result:
[
    { name: 'Alice', age: 25 },
    { name: 'Bob', age: 30 },
    { name: 'Charlie', age: 35 }
]
*/

const fruitsName = ["Banana", "apple", "Cherry"];

fruitsName.sort((a, b) => a.localeCompare(b));
console.log(fruitsName);

// Result: ['apple', 'Banana', 'Cherry'] (sorts correctly considering capitalization)

//sort the array based on its string elements length
const names = ["bob", "alice", "jane", "doe"];

names.sort((a, b) => a.length - b.length);
console.log("Names: ", names);
