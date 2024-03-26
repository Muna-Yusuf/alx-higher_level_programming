#!/usr/bin/node
// Script that prints the title of a Star Wars movie where..
// the episode number matches a given integer.

const filesys = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

filesys.get(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
