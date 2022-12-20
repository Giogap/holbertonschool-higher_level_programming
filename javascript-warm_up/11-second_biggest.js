#!/usr/bin/node

const len = process.argv.length - 2;

if (len < 2 || isNaN(len)) {
    console.log(0);
}
