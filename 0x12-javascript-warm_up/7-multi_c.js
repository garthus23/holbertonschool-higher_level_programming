#!/usr/bin/node

let i = 0;

if (process.argv[2] && parseInt(process.argv[2])) {
  while (i !== parseInt(process.argv[2])) {
    console.log('C is fun');
    i += 1;
  }
} else {
  console.log('Missing number of occurences');
}
