#!/usr/bin/node
/* 
 * Script to print an integer
 */

const { argv } = require('process');
const firstArgument = argv[2];

if (isNaN(firstArgument)) {
	console.log("Not a number");
} else {
	console.log(`My number: ${firstArgument}`);
}
