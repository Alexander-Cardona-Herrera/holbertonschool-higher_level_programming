#!/usr/bin/node
/* Task 7 */

let i = 0;

if (Number.isInteger(parseInt(process.argv[2])) === true) {
  while (i < parseInt(process.argv[2])) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
