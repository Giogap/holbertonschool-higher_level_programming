#!/usr/bin/node

var fs = require("fs");

fs.readFile('cisfun', 'utf8', function(err, data) {
    console.log(data);
});