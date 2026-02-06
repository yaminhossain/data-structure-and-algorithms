//Loop through an array

const arr = [1, 2, 3];

//using index
for (i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}

console.log("====================================");

//using for of loop
for(n of arr){
  console.log(n);
}

console.log("====================================");

//Using forEach loop
const fruits = ["apple", "banana", "cherry"];

fruits.forEach((item, index) => {
  console.log(`${index}: ${item}`);
});
