#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
    for (const character of characters) {
      request.get(character, (err, response, body) => {
        if (err) {
          console.error(err);
        } else {
          const name = JSON.parse(body).name;
          console.log(name);
        }
      });
    }
  }
});
