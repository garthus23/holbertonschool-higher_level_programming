#!/usr/bin/node

if (!process.argv[2]) {
  console.log('Not a number');
} else {
  if (Number(process.argv[2])) {
    console.log('My number : ' + Number(process.argv[2]));
  } else {
    console.log('Not a number');
  }
}
