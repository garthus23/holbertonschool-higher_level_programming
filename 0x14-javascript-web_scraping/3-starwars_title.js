#!/usr/bin/node

let movie;

if (process.argv.length === 3) {
  const request = require('request');
  request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, function (error, response, body) {
    if (error) {
      return console.error(error);
    }
    movie = JSON.parse(body);
    console.log(movie.title);
  });
}
