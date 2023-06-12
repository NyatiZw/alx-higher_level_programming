#!/usr/bin/node

const { argv } = require('process');
const firstArgument = argv[2];
const secondArgument = argv[3];

if (firstArgument === undefined && secondArgument === undefined) {
	console.log("undefined is undefined");
} else if (firstArgument !== undefined && secondArgument === undefined) {
	console.log(`${firstArgument} is undefined`);
} else {
	console.log(`${firstArgument} is ${secondArgument}`);
}
