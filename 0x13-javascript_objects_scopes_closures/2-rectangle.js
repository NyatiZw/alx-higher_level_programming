#!/usr/bin/node
// Class definition of a rectangle

module.exports = class Rectangle {
	constructor (w, h) {
		if ((w % 1 !== 0) || (h % 1 !== 0) || w <= 0 || h <= 0) {
		this.width = w;
		this.height = h;
		}
	}
};
