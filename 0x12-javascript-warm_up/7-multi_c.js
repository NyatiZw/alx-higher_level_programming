#!/usr/bin/node
/* 
 * Script to print an integer
 */

const { argv } = require('process');
const x = argv[2];
const a = "C is fun";

if (isNaN(x)) {
	console.log("Missing number of occurrences");
} else {
	let count = +x;
	while (count > 0) {
		console.log(a);
		count--;
	}
}
