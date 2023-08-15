#!/usr/bin/node
// A function that returns the reversed version of a list
exports.esrever = function (list) {
  const rlist = [];
  let j = 0;
  for (let i = list.length; i > 0; i--) {
    rlist[j++] = list[i - 1];
  }
  return rlist;
};
