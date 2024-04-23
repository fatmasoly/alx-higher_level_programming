#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
request.get(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile('store.json', response.body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
