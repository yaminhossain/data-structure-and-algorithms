const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("Enter your age: ", (age) => {
  console.log(age);
  rl.close();
});

/*
 *rl.question() is callback-based.
 *It does not return the terminal input rather input can be found inside the callback.
 *The terminal value is stream. So, it receives chunk by chunk asynchronously where rl.close() finalize the last received data.
 */
