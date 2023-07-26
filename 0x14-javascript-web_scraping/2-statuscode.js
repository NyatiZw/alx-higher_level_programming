#!/usr/bin/node
// Script that writes a string to a file

const request = require('request');

function displayStatusCode(url) {
  request.get(url, (error, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}

// Check if the file path argument is provided
if (process.argv.length < 3) {
  console.error(error);
} else {
  const url = process.argv[2];
  displayStatusCode(url);
}
