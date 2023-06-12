#!/usr/bin/node
import process from 'node:process';

let args = process.agrv;

if (args.length === 1) {
	console.log("Argument found\n");
} else if (args.length === 0) {
	console.log("Arguments not found\n");
} else if (args.length > 1) {
	console.log("Arguments found\n");
}
