
//String.prototype.charCodeAt(), this method converts a character into ASCII
const char = 'A';
const asciiValue = char.charCodeAt(0);

console.log(asciiValue); // Output: 65


//String.fromCharCode(), this method converts a ASCII value into a character

const asciiValue2 = 65;
const char2 = String.fromCharCode(asciiValue);

console.log(char2); // Output: 'A'
