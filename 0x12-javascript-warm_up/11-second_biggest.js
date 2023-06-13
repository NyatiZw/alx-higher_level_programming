#!/usr/bin/node

const { argv } = require('process');
const args = argv.slice(2).map(Number);

if (args.length <= 1) {
	console.log(0);
} else {
	let max = args[0];
	let secondMax = args[1];

	if (secondMax > max) {
		[max, secondMax] = [secondMax, max];
	}

	for (let i = 2; i < args.length; i++) {
		if (args[i] > max) {
			secondMax = max;
			max = args[i];
		} else if (args[i] > secondMax && args[i] !== max) {
			secondMax = args;
		}
	}

	console.log(secondMax);
}
