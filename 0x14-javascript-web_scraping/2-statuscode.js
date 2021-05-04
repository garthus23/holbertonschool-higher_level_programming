#!/usr/bin/node

if (process.argv.length === 3) {
  const request = require('request');
  request(process.argv[2], function (error, response, body) {
    if (error) {
      return console.error(error);
    }
    console.log('code:', response && response.statusCode);
  });
}
