#!/usr/bin/node
/* Task 10 */

exports.converter = function (base) {
  return function (x) {
    return (x.toString(base));
  };
};
