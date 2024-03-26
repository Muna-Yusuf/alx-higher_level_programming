#!/usr/bin/node
// Script that display the status code of a GET request.

const filesys = require('request');
const url = process.argv[2];

filesys.get(url, function (err, resp) {
  if (err) {
    console.log(err);
  } else {
    console.log('code:' + ' ' + resp.statusCode);
  }
});
