#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (x) {
  for (let i = 0; i < x; i++) {
    console.log('X');
    for (let j = 0; j < x; j++) {
      console.log('X')
    }
  }
} else {
  console.log('Missing size');
}
