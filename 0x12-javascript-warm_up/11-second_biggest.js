#!/usr/bin/node
const { argv } = require('process');

// check if there is argv
if (!argv[2] || !argv[3]) {
  console.log(0);
} else {
  let m = 4;
  let max = parseInt(argv[2], 10);
  let max2 = parseInt(argv[3], 10);

  if (max2 > max) {
    [max, max2] = [max2, max];
  }
  do {
    const next = parseInt(argv[m], 10);
    if (max < next) {
      max2 = max;
      max = next;
    } else if (next > max2 && next !== max) {
      max2 = next;
    }
    m++;
  } while (argv[m]);
  console.log(max2);
}
