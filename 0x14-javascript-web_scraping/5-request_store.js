#!/usr/bin/node

let text;

if (process.argv.length === 4) {
  const request = require('request');
  request(process.argv[2], function (error, response, body) {
    if (error) {
      return console.error(error);
    }
    text = ('body:', body);
    console.log(text);
    const fs = require('fs');
    fs.writeFile(process.argv[3], text, 'utf8', function (err) {
      if (err) {
        return console.error(err);
      }
    });
  });
}
