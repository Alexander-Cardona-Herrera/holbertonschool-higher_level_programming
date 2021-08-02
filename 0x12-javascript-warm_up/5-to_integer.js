#!/usr/bin/node
/* Task 5 */

if (Number.isInteger(parseInt(process.argv[2])) === true) {
  const myVar = parseInt(process.argv[2]);
  console.log('My number: ' + myVar);
} else {
  console.log('Not a number');
}
