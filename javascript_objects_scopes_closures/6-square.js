#!/usr/bin/node

const Sqr = require('./5-square');

module.exports = class Square extends Sqr {
  charPrint(c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        console.log('C'.repeat(this.width));
          } 
    } else {
        for (let i = 0; i < this.height; i++) {
          console.log((c = 'X').repeat(this.width));
        }
    }           
  }
};