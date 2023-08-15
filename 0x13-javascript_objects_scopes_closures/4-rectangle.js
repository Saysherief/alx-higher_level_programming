#!/usr/bin/node
// A class Rectangle that defines a rectangle
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Function that prints
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // Function that Rotates
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  // Function that Doubles size
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
