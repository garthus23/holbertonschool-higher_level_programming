#!/usr/bin/node

let i = 4;
let max;
let middle;
if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  if (parseInt(process.argv[2]) > parseInt(process.argv[3])) {
    max = parseInt(process.argv[2]);
    middle = parseInt(process.argv[3]);
  } else {
    max = parseInt(process.argv[3]);
    middle = parseInt(process.argv[2]);
  }
  while (process.argv[i]) {
    if (parseInt(process.argv[i]) > max) {
      middle = parseInt(max);
      max = parseInt(process.argv[i]);
    } else if (parseInt(process.argv[i]) > middle) {
      middle = parseInt(process.argv[i]);
    }
    i++;
  }
  console.log(middle);
}
