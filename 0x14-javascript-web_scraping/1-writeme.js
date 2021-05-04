#!/usr/bin/node

var fs = require("fs");
file = process.argv[2];
fs.readFile(file, function (err, data) {
      if (err) {
         return console.error(err);
      }
      process.stdout.write(data.toString());
});
