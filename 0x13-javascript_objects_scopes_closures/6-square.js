#!/usr/bin/node
// A class Square that defines a square and inherits from Square of 5-square.js
const Square1 = require('./5-square');

class Square extends Square1 {
  // A function that prints based on a given character
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
