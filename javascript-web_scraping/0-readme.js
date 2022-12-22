#!/usr/bin/node

let fs = require("fs");

fs.readFile('cisfun', 'utf8', function(err, data) {
    console.log(data);
});