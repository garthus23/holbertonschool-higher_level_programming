#!/usr/bin/node

let i;
if (parseInt(process.argv[2]) > 0) {
  for (i = 0; i != process.argv[2]; i++) {
    console.log('X'.repeat(process.argv[2]));
  }
} else {
  console.log('Missing size');
}
