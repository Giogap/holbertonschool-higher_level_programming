#!/usr/bin/node

let numItem = 0;
exports.logMe = function (item) {
  console.log(numItem + ': ' + item);
  numItem++;
}
