#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    return console.error(err);
  }
  const dict = {};
  for (let newid = 1; newid <= 10; newid++) {
    let count = 0;
    for (const tasks of JSON.parse(body)) {
      if (tasks.userId === newid) {
        if (tasks.completed === true) {
          count++;
        }
      }
    }
    if (count !== 0) {
      dict[newid] = count;
    }
  }
  console.log(dict);
});
