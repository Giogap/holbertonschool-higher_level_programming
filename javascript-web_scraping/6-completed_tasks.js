#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(body);
    const task = {};
    for (const x of todos) {
      if (x.completed === true) {
        if (x.userId in task) {
          task[x.userId]++;
        } else {
          task[x.userId] = 1;
        }
      }
    }
    console.log(task);
  }
});
