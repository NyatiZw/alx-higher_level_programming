#!/usr/bin/node
// Script that writes a string to a file

const fs = require('fs');
const request = require('request');

function fetchAndStore(Url, filePath) {
  request.get(Url, { encoding: 'utf-8' }, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      fs.writeFile(filePath, body, 'utf-8', (err) => {
        if (err) {
          console.error(err);
        }
      });
    }
  });
}

// Check if the file path argument is provided
if (process.argv.length < 4) {
  console.error(error);
} else {
  const url = process.argv[2];
  const filePath = process.argv[3];
  fetchAndStore(url, filePath);
}
