import readline from "readline";
import { stdin, stdout } from "process";

function ask(question) {
  const rl = readline.createInterface({ input: stdin, output: stdout });
  return new Promise((resolve) =>
    rl.question(question, (answer) => {
      rl.close();
      resolve(answer);
    }),
  );
}

const name = await ask("Name: ");
console.log(name);

let age;
age = await ask("Enter your age: ");
console.log(parseInt(age));

/*
 *rl.question() is callback-based. It does not return the terminal input rather input can be found inside the callback.
 *The terminal value is stream. So, it receives chunk by chunk asynchronously where rl.close() finalize the last received data.
 *Inside ES6 module, we can use await keyword without the async function.
 *new Promise() creates a promise where resolve() returns a value when the promise will be resolved by await keyword.
 */