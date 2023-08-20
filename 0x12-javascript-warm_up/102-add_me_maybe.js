#!/usr/bin/node
// A function that increments and calls
const addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};

module.exports = {
  addMeMaybe: addMeMaybe
};
