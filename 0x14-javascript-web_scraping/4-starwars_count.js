#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    return console.error(err);
  }
  let count = 0;
  for (const wedge of JSON.parse(body).results) {
    for (const antilles of wedge.characters) {
      if (antilles.endsWith('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
