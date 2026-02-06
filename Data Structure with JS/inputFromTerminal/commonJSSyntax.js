const readline = require("readline");
const { stdin, stdout } = require("process");

function ask(question) {
  const rl = readline.createInterface({ input: stdin, output: stdout });
  return new Promise((resolve) =>
    rl.question(question, (answer) => {
      rl.close();
      resolve(answer);
    }),
  );
}

const inputHandler = async () => {
  let name = await ask("Enter your name:");
  console.log(name);

  const age = await ask("Age: ");
  console.log(age);
};

inputHandler();

/*
 *rl.question() is callback-based. It does not return the terminal input rather input can be found inside the callback.
 *The terminal value is stream. So, it receives chunk by chunk asynchronously where rl.close() finalize the last received data.
 *new Promise( ) creates a promise where resolve() returns a value when the promise will be resolved inside inputHandler.
 */
