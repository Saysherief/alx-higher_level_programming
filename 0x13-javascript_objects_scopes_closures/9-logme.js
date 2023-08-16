#!/usr/bin/node
// A function that prints the number of arguments already printed and the new argument value
exports.logMe = function (item) {
  if (typeof exports.logMe.logNo === 'undefined') {
    exports.logMe.logNo = 0;
  }

  console.log(exports.logMe.logNo + ': ' + item);
  exports.logMe.logNo++;
};
