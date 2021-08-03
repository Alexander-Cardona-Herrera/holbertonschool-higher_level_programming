#!/usr/bin/node
/* Task 6 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    let i = 0;
    if (!c) {
      while (i < this.size) {
        console.log('X'.repeat(this.size));
        i++;
      }
    } else {
      while (i < this.size) {
        console.log(c.repeat(this.size));
        i++;
      }
    }
  }
}
module.exports = Square;
