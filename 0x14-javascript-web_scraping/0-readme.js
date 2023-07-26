#!/usr/bin/node
// Script that reads and prints the content of a file

const fs = require('fs');
filePath = process.argv[2];

function readFileContent(filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
}

readFileContent(filePath);
