#!/usr/bin/node

const SquareOg = require('./5-square');

class Square extends SquareOg {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(String(c).repeat(this.width));
      }
    }
  }
}

module.exports = Square;
