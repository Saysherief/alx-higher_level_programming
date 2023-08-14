#!/usr/bin/node
const { argv } = require('process');

// Returns the addition of 2 integers
function add (a, b) {
  return a + b;
}
console.log(add(parseInt(argv[2], 10), parseInt(argv[3], 10)));
