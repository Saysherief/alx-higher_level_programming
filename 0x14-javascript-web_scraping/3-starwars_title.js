#!/usr/bin/node
const request = require('request');
const titleId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${titleId}`;
request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error('Error:', err.message);
  } else {
    const title = JSON.parse(body);
    console.log(`${title.title}`);
  }
});
