//Strings are similar to arrays

const s = "abc";
console.log(s.slice(0, 2)); //ab

console.log(s[0]); //a

//Strings are immutable in JavaScript, This means that once a string value is created, it cannot be changed. 
s[2] = "e";
console.log(s);//abc

//This creates a new string. As strings are immutable it acts like primitives as well.
const x = s+ "def"
console.log(s); //abc
console.log(x); //abcdef