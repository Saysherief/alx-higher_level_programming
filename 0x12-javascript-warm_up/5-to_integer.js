#!/usr/bin/node
const { argv } = require('process');

// check if there is argv or is a number
if (!argv[2] || isNaN(argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(argv[2], 10));
}
