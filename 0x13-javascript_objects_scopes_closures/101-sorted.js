#!/usr/bin/node
/* Task 101 */

const newDict = require('./101-data').dict;

const newDict2 = {};

for (const key in newDict) {
  if (!newDict2[newDict[key]]) {
    newDict2[newDict[key]] = [];
  }
  newDict2[newDict[key]].push(key);
}

console.log(newDict2);
