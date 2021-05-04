#!/usr/bin/node

if (process.argv.length === 3) {
  const fs = require('fs');
  fs.readFile(process.argv[2], function (err, data) {
    if (err) {
      return console.error(err);
    }
    process.stdout.write(data.toString());
  });
}
