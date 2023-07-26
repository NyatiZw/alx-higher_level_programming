#!/usr/bin/node
// Script that writes a string to a file

const fs = require('fs');

function writeFileContent(filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    } else {
      console.log('Content has been successfully written to the file');
    }
  });
}

// Check if the file path argument is provided
if (process.argv.length < 4) {
  console.error(err);
} else {
  const filePath = process.argv[2];
  const content = process.argv[3];
  writeFileContent(filePath, content);
}
