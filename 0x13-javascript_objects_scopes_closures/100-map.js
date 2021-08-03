#!/usr/bin/node
/* Task 100 */

const list = require('./100-data');
const newlist = list.list;

const map1 = newlist.map((element, index) => element * index);
console.log(newlist);
console.log(map1);
