// ========================= Creating and Populating a Map ==============

const inventory = new Map();
inventory.set("apples", 500);
inventory.set("bananas", 400);
inventory.set("oranges", 600);
// console.log(inventory.size);

// =========================== Accessing Values =================

const appleCount = inventory.get("apples");
console.log(`We have ${appleCount} apples.`); // Output: We have 500 apples.

const grapesCount = inventory.get("grapes");
console.log(`Grapes count: ${grapesCount}`); // Output: Grapes count: undefined

// ============================== Checking for Key Existence ======================

if (inventory.has("bananas")) {
  console.log("Bananas are in stock.");
}

// ================================= Looping =====================================

// Using forEach
inventory.forEach((value, key) => {
  console.log(`${key}: ${value}`);
});

// Using a for...of loop for entries [key, value]
for (const [key, value] of inventory.entries()) {
  console.log(`${key} -> ${value}`);
}

// =========================== Tuples can be used as key ====================
const testMap = new Map();
testMap.set([1, 2], "Yamin");
testMap.set([2, 4], "Hossain");

console.log("Test Map: ", testMap); // { [ 1, 2 ] => 'Yamin', [ 2, 4 ] => 'Hossain' }

// ========================= More methods ============================
const markSheet = new Map();

markSheet.set("Yamin", 100);
markSheet.set("Hossain", 600);

console.log([...markSheet.entries()]);
