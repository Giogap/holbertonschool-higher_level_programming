#!/usr/bin/node

const len = process.argv.length - 2;
const array = process.argv.slice(0)

if (len < 2 || isNaN(len)) {
    console.log(0);
} else {
    array.sort();
    console.log(array[len])
}
