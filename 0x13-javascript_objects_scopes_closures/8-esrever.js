#!/usr/bin/node
/* Task 8 */

exports.esrever = function (list) {
  const arr = [];
  let x = list.length - 1;
  while (x >= 0) {
    arr.push(list[x]);
    x--;
  }
  return arr;
};
