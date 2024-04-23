#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
    if (error) {
        console.error(error);
    } else if (response.statusCode === 200) {
        const film = JSON.parse(body);
        const characters = film.characters;

        characters.forEach(characterUrl => {
            request.get(characterUrl, (err, res, body) => {
                if (err) {
                    console.error(err);
                } else if (res.statusCode === 200) {
                    const character = JSON.parse(body);
                    console.log(character.name);
                } else {
                    console.error(`Failed to fetch character details. Status code: ${res.statusCode}`);
                }
            });
        });
    } else {
        console.error(`Failed to fetch movie details. Status code: ${response.statusCode}`);
    }
});
