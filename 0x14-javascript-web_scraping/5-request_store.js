#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.

const filesys = require('fs');
const request = require('request');

request.get(process.argv[2], (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    filesys.writeFile(process.argv[3], body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
