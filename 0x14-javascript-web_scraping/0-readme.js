#!/usr/bin/node
// A script that reads and prints the content of a file
const fs = require('fs');
const filePath = process.argv[2];
fs.readFile(filePath, 'utf-8', (err, inputD) => {
  console.log(err || inputD);
});
