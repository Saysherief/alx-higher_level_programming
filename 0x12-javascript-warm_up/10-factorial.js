#!/usr/bin/node
const { argv } = require('process');

// Returns the nth factorial
function fact (n) {
  if (n === 1 || n === 0) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}
if (!argv[2] || isNaN(argv[2])) {
  console.log(1);
} else {
  console.log(fact(parseInt(argv[2], 10)));
}
