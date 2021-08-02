#!/usr/bin/node
/* Task 11 */

function nextBiggest (arr) {
  let max = -Infinity; let result = -Infinity;

  for (const value of arr) {
    const nr = Number(value);

    if (nr > max) {
      [result, max] = [max, nr]; // save previous max
    } else if (nr < max && nr > result) {
      result = nr; // new second biggest
    }
  }
  return result;
}

if (!process.argv[2]) {
  console.log(0);
} else if (!process.argv[3]) {
  console.log(0);
} else {
  const arr = [];
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(process.argv[i]);
  }
  console.log(nextBiggest(arr));
}
