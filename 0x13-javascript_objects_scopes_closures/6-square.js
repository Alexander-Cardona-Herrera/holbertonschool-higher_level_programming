#!/usr/bin/node
/* Task 6 */

class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let i = 0;
    if (!c) {
      while (i < this.width) {
        console.log('X'.repeat(this.width));
        i++;
      }
    } else {
      while (i < this.width) {
        console.log(c.repeat(this.width));
        i++;
      }
    }
  }
}
module.exports = Square;
