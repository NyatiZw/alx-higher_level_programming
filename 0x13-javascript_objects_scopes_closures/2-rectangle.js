#!/usr/bin/node
// Class definition of a rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 && h <= 0) {
      return {};
    }
    this.width = w;
    this.height = h;
  }
};
