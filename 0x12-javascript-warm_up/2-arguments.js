#!/usr/bin/node
// import { argv } from 'node:process';...didn't work
const { argv } = require('process');

// check if there is argv
if (!argv[2]) {
  console.log('No argument');
} else if (!argv[3]) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
