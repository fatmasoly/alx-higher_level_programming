#!/usr/bin/node
const request = require('request');
const movie_ID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movie_ID;
request.get(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(response.body).title);
  }
});
