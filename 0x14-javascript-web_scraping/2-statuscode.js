#!/usr/bin/node
// A script that displays the status code of a GET request
const request = require('request');
const url = process.argv[2];
request.get(url, (err, response) => {
  if (err) {
    console.error('Error:', err.message);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
