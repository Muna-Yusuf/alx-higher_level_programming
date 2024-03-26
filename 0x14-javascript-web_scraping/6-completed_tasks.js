#!/usr/bin/node
// Script that computes the number of tasks completed by user id.

const request = require('request');

request.get(process.argv[2], { json: true }, (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const compltasks = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!compltasks[todo.userId]) {
        compltasks[todo.userId] = 1;
      } else {
        compltasks[todo.userId] += 1;
      }
    }
  });
  console.log(compltasks);
});
