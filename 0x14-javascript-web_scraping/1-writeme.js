#!/usr/bin/node

if (process.argv.length === 4) {
  const fs = require('fs');
  fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (err) {
    if (err) {
      return console.error(err);
    }
  });
}
