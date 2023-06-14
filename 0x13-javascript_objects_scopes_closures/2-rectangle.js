#!/usr/bin/node
// Class definition of a rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w && h === 0) || (w && h < 0)) {
      return Rectangle();
    }
    this.width = w;
    this.height = h;
  }
};
