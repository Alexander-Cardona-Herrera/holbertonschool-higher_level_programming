#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + parseInt(process.argv[2]);
request(url, function (err, response, body) {
  if (err) {
    return console.error(err);
  }
  console.log(JSON.parse(body).title);
});
