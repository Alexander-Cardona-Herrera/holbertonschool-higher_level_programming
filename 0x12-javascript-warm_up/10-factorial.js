#!/usr/bin/node
/* Task 9 */

function fact (a) {
  if (!a) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}
console.log(fact(parseInt(process.argv[2])));
