#!/usr/bin/node
/* Task 102 */

exports.addMeMaybe = function (number, theFunction) {
  const nb = number + 1;
  theFunction(nb);
};
