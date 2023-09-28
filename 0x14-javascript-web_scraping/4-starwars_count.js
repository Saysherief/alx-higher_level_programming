#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error('Error:', err.message);
  } else {
    const myResult = JSON.parse(body).results;
    console.log(myResult.reduce((count, movie) => {
      return movie.characters.find((charac) => charac.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
