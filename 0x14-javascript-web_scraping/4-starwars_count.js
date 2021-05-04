#!/usr/bin/node

let i = 1;
var result= 0;

if (process.argv.length === 3) {
    for (i=1; i <= 7; i++) {
        const request = require('request');
        url = process.argv[2] + '/' + i
        request(url, function (error, response, body) {
            let j = 0;
            if (error) {
              return console.error(error);
            }
            movie = JSON.parse(body);
            for (const [key, value] of Object.entries(movie.characters)) {
                if (value === 'https://swapi-api.hbtn.io/api/people/18/') {
                    result++;
                }
            }
            
            console.log(result);
        });
    }
}
