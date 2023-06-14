#!/usr/bin/node

const SquareOriginal = require('./5-square');
class Square extends SquareOriginal {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('c'.repeat(this.width));
      }
    }
  }
}


module.exports = Square;
