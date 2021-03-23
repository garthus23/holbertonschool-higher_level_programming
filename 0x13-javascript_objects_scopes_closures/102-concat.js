#!/usr/bin/node

const fs = require('fs');

if (process.argv[2] && process.argv[3] && process.argv[4]) {
  fs.readFile(process.argv[2], 'utf-8', (err, data) => {
    if (err) throw err;
    fs.writeFile(process.argv[4], data, (err) => {
      if (err) throw err;
    });
  });
  fs.readFile(process.argv[3], 'utf-8', (err, data) => {
    if (err) throw err;
    fs.appendFile(process.argv[4], data, (err) => {
      if (err) throw err;
    });
  });
}
