#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/'
const moveId = process.argv[2];

 request.get(url + moveId, (err, res, body) => { 
   if (err) {
    console.log(err)
   } else {
    console.log(JSON.parse(body).title);
   }
 });
