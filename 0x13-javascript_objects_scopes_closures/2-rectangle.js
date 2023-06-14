#!/usr/bin/node
// Class definition of a rectangle

module.exports = class Rectangle {
	width: number;
	height: number;

	constructor(w: number, h: number) {
		this.width = w;
		this.height = h;
	}
};
