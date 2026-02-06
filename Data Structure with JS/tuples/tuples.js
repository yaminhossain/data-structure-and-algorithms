// Tuples are like arrays but immutable collection of elements. Unlike arrays, tuples cannot be modified after creation.

"use strict";
const tuple = [1, 3, 4];
Object.freeze(tuple);

// Can't modify
// tuple[0] = 5;
console.log(tuple[0]); //1
console.log(tuple[tuple.length - 1]); //4
