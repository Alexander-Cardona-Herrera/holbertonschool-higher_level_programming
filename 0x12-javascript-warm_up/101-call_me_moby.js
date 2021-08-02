#!/usr/bin/node
/* Task 101 */

exports.callMeMoby = function (x, theFunction) {
  let i = 0;
  while (i < x) {
    theFunction();
    i++;
  }
};
