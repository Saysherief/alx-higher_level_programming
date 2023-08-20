#!/usr/bin/node
// A function that executes x times a function
const callMeMoby = function (x, theFunction) {
  for (let n = 0; n < x; n++) {
    theFunction();
  }
};

module.exports = {
  callMeMoby: callMeMoby
};
