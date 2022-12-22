#!/usr/bin/node

let fs = require("fs");
let FileName = process.argv[2];

fs.readFile(FileName, 'utf8', function(err, data) {
    if (data) {
      console.log(data);
    } else {
        console.log(err)
    }    
});