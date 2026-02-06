const { Deque } = require("@datastructures-js/deque");
const deque = new Deque([1, 2, 3, 4]);
deque.pushFront(7);
deque.pushBack(9);

deque.popFront();
deque.pushFront(10)

console.log(deque.toArray());
