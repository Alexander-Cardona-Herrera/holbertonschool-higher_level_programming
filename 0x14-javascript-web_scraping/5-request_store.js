#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (err, data) {
  if (err) {
    return console.error(err);
  }
  fs.writeFile(process.argv[3], data.body, 'utf8', (err) => {
    if (err) {
      return console.error(err);
    }
  });
});
