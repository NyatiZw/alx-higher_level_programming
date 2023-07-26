#!/usr/bin/node
// Script that writes a string to a file

const request = require('request');

function getMovieTitle(movieId) {
  const apiUrl = 'https://swapi-api.alx-tools.com/api/films/${movieId}';

  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    }
  });
}

// Check if the file path argument is provided
if (process.argv.length < 3) {
  console.error(error);
} else {
  const movieId = process.argv[2];
  getMovieTtile(movieId);
}
