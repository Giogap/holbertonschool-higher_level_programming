#!/usr/bin/node

const len = process.argv.length - 2;
const array = process.argv.slice(2);

if (len < 2 || isNaN(len)) {
  console.log(0);
} else {
    array.sort(num);
    console.log(array[len - 2]);
}
function num (a, b) {
  return a - b;
}
