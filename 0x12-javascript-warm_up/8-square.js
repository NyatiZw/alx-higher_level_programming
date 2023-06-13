#!/usr/bin/node
/* 
 * Script to print an integer
 */

const { argv } = require('process');
const size = argv[2];
const a = "x";

if (isNaN(size)) {
	console.log("Missing size");
} else {
	let count = +size;
	let line = 0;
	while (line < count) {
		let row = "";
		for (let i = 0; i < count; i++) {
			row += a;
		}
		console.log(row);
		line++;
	}
}
