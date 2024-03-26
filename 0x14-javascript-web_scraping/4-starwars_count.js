#!/usr/bin/node
// Script that prints the number of movies where the ...
// ... character “Wedge Antilles” is present.

const filesys = require('request');
let num = 0;

filesys.get(process.argv[2], (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    content.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          num += 1;
        }
      });
    });
    console.log(num);
  }
});
