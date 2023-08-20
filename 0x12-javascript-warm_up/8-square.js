#!/usr/bin/node
const { argv } = require('process');

// check if there is argv
if (!argv[2] || isNaN(argv[2])) {
  console.log('Missing size');
} else {
  const myVar = 'X';
  let n = 0; let m = 0;
  let mySq = '';
  const size = parseInt(argv[2], 10);
  while (n < size) {
    while (m < size) {
      mySq += myVar;
      m++;
    }
    console.log(mySq);
    n++;
  }
}
