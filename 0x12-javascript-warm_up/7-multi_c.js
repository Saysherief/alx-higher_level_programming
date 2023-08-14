#!/usr/bin/node
const { argv } = require('process');

// check if there is argv
if (!argv[2] || isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const myVar = 'C is fun';
  let n = 0;
  while (n < parseInt(argv[2], 10)) {
    console.log(myVar);
    n++;
  }
}
