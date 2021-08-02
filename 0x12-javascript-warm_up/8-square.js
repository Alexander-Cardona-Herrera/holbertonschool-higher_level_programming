#!/usr/bin/node
/* Task 8 */

let i = 0;

if (Number.isInteger(parseInt(process.argv[2])) === true) {
  while (i < parseInt(process.argv[2])) {
    console.log('X'.repeat(parseInt(process.argv[2])));
    i++;
  }
} else {
  console.log('Missing size');
}
