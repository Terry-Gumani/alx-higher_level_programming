#!/usr/bin/node
function incrementAndCall(number, theFunction) {
  let incrementedNumber = number + 1;
  theFunction(incrementedNumber);
}

// Example usage:
function exampleFunction(result) {
  console.log(`The result is ${result}`);
}

incrementAndCall(5, exampleFunction); // Output: The result is 6

