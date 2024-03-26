#!/usr/bin/node
// Script that prints all characters of a Star Wars movie.

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
    for (const ch of characters) {
      request.get(ch, (err, resp, body) => {
        if (err) {
          console.log(err);
        } else {
          const n = JSON.parse(body);
          console.log(n.name);
        }
      });
    }
  }
});
