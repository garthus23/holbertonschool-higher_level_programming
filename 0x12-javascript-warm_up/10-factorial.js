#!/usr/bin/node

function factorial (number) {
  if (number) {
    return (number * factorial(number - 1));
  } else {
    return 1;
  }
}

console.log(factorial(process.argv[2]));
