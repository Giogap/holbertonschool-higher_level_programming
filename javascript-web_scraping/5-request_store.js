#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, 'utf8', function (err, res, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(filePath, body, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});

