const { MinHeap } = require("@datastructures-js/heap");

//constructor
const numberHeap = new MinHeap(null, [3, 1, 5, 6, 7, 3]);
numberHeap.insert(5).push(6).insert(7);
numberHeap.extractRoot();
numberHeap.extractRoot();
console.log(numberHeap.root());
console.log(numberHeap.toArray());
