#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;
request.get(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(response.body).title);
  }
});
