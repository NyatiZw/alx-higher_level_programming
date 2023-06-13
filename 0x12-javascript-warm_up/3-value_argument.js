#!/usr/bin/node

const { argv } = require('process');

if (argv[2] === undefined) {
  console.log('No argument');
} else {
  const firstArgument = argv[2];
  console.log(firstArgument);
}
