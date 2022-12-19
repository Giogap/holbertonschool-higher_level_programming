#!/usr/bin/node

import { argv } from 'node:process';

// print process.argv
argv.forEach((val, index) => {
    if (argv = null) {
        console.log('No argument');
    }
    else if (argv = 1) {
        console.log('Argument found');
    }
    else {
        console.log('Arguments found')
    }
  
});


console.log(process.argv);