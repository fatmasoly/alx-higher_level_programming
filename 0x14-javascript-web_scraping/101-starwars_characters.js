#!/usr/bin/node

const args = process.argv;
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;

request(url, async (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const moviesCharacters = JSON.parse(body).characters;

  const names = [];
  for (const character of moviesCharacters) {
    try {
      const characterData = await new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
          if (error) reject(error);
          else resolve(JSON.parse(body).name);
        });
      });
      names.push(characterData);
    } catch (err) {
      console.error(err);
    }
  }

  names.forEach((name) => {
    console.log(name);
  });
});
